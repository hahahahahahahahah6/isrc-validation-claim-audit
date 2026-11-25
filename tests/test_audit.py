import tempfile
import contextlib
import io
from isrc_validation_claim_audit.audit import main
import unittest
from pathlib import Path
from isrc_validation_claim_audit.audit import audit, claims, evidence
from isrc_validation_claim_audit.phrases import ISRCVALIDATION, NOISRCVALIDATION, GENERIC_NAMES


class AuditTests(unittest.TestCase):
    def test_phrases(self):
        self.assertEqual((len(set(ISRCVALIDATION)), len(set(NOISRCVALIDATION)), len(set(GENERIC_NAMES))), (50, 24, 24))
        for phrase in ISRCVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (True, False))
        for phrase in NOISRCVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (False, True))
        self.assertEqual(claims('```\nvalidate isrc\n```'), (False, False))
        self.assertEqual(claims('~~~ text\nvalidate isrc\n~~~'), (False, False))
        self.assertEqual(claims('`validate-isrc`'), (True, False))
        self.assertEqual(claims("doesn't validate isrc"), (False, True))
        self.assertEqual(claims('validate isrcXYZ'), (False, False))

    def test_library_routes(self):
        for method in ('validate', 'is_valid'):
            for prefix, call in [('import stdnum.isrc', 'stdnum.isrc.' + method), ('import stdnum.isrc as im', 'im.' + method), ('from stdnum import isrc', 'isrc.' + method), ('import stdnum', 'stdnum.isrc.' + method), ('from stdnum.isrc import ' + method, method), ('from stdnum.isrc import ' + method + ' as v', 'v')]:
                with self.subTest(method=method, call=call): self.assertTrue(evidence(prefix + '\n' + call + '(x)'))

    def test_generic_routes(self):
        for name in GENERIC_NAMES:
            for source in ('obj.' + name + '(x)', 'from lib import ' + name + ' as f\nf(x)', 'obj = factory()\nobj.' + name + '(x)'):
                with self.subTest(source=source): self.assertTrue(evidence(source))

    def test_not_evidence(self):
        cases = ['import stdnum.isrc', 'validate(x)', 'is_valid(x)', 'validate_isrc(x)', 'obj.validate(x)', 'obj.isrc(x)', 'import stdnum.isrc\nstdnum.isrc.compact(x)', 'import stdnum.isrc\nstdnum.isrc.format(x)', 'from stdnum import ean\nean.validate(x)', 'from stdnum import ean\nean.calc_check_digit(x)', 'from stdnum import luhn\nluhn.validate(x)', 'from stdnum import luhn\nluhn.calc_check_digit(x)', 'import re\nre.match(x,y)', 'import re\nre.search(x,y)', 'import re\nre.fullmatch(x,y)', 'len(x) == 12', 'issuer in known', 'validators.isrc(x)', 'lookup.isrc(x)', '"validate isrc"', 'validate_isrc', 'def broken(:', 'import subprocess\nsubprocess.run(["isrc-check"])', 'import stdnum.isrc as im\nim = x\nim.validate(x)', 'from stdnum.isrc import validate\nwith x as validate:\n validate(x)', 'def validate_isrc(x): pass\nobj.validate_isrc(x)']
        cases += ['isrc(x)', 'compact(x)', 'format(x)', 'obj.is_valid(x)', 'obj.compact(x)', 'obj.format(x)', 'import validators\nvalidators.isrc(x)', 'import stdnum.isrc as gr\nwith ctx() as gr:\n gr.validate(x)', 'from lib import validate_isrc as v\nv = other\nv(x)', 'class C:\n def validate_isrc(self): pass\nobj.validate_isrc(x)', '# validate isrc\nx = \"isrc validation\"']
        cases += ['from stdnum import ' + n + '\n' + n + '.validate(x)' for n in ('isbn', 'issn', 'ismn', 'isan', 'isin')]
        for source in cases:
            with self.subTest(source=source): self.assertFalse(evidence(source))

    def test_findings(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d); (p/'README.md').write_text('validate isrc')
            self.assertEqual(audit(p)[0]['severity'], 'HIGH')
            (p/'tests').mkdir(); (p/'tests/test_a.py').write_text('obj.validate_isrc(x)')
            self.assertEqual(audit(p)[0]['severity'], 'MEDIUM')
            (p/'a.py').write_text('obj.validate_isrc(x)')
            self.assertEqual(audit(p), [])
            (p/'README.md').write_text('does not validate isrc')
            self.assertEqual(audit(p)[0]['severity'], 'HIGH')
            (p/'a.py').unlink(); self.assertEqual(audit(p), [])
            (p/'README.md').write_text('validate isrc')
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(['audit', str(p)]), 0)
                self.assertEqual(main(['audit', str(p), '--fail-on', 'medium']), 2)
                self.assertEqual(main(['audit', str(p), '--ignore', 'tests']), 2)
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main(['audit', str(p/'missing')]), 1)

    def test_exclusions(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d); (p/'README.md').write_text('validate isrc')
            for folder in ('fixtures', 'docs', 'examples'):
                (p/folder).mkdir(); (p/folder/'a.py').write_text('obj.validate_isrc(x)')
            (p/'link.py').symlink_to(p/'fixtures/a.py')
            self.assertEqual(audit(p)[0]['severity'], 'HIGH')
            (p/'src.py').write_text('obj.validate_isrc(x)')
            self.assertEqual(audit(p, ['src.py'])[0]['severity'], 'HIGH')
