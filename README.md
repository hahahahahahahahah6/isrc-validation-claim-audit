# Recording-code claim audit

This offline static audit compares documented recording-code capability claims with Python call patterns. It does not execute the inspected source or contact a network. An International Standard Recording Code has a two-letter country code, three-character registrant, two-digit year and five-digit designation; it has no check digit.

## Install and use

```sh
python3 -m pip install .
isrc-validation-claim-audit audit .
python3 -m isrc_validation_claim_audit audit . --json
```

The optional repository argument defaults to the current directory. Use `--ignore PREFIX` repeatedly to exclude relative path prefixes, `--fail-on medium` to include test-only findings in the exit threshold, `--verbose` for the path, and `--json` for machine-readable output. Exit status is 0 for a pass at the selected threshold, 2 for findings at or above it, and 1 for usage or input errors. The default threshold is high. Version information is available with `--version`.

## Findings

```
documented-isrc-validation-claim-false
documented-no-isrc-validation-claim-false
```

A positive claim without production evidence is high severity, or medium when evidence occurs only in tests. A denial with production evidence is high severity. A denial without source evidence passes.

Root README and Markdown files beneath a docs directory supply claims; fenced blocks are excluded and inline code counts. The scanner normalizes case, whitespace, contractions and hyphens and matches exact phrases. Denial spans are removed before positive matching. Python files are parsed without execution; fixtures, examples and docs are excluded from source evidence, and tests are tracked separately. Symlinks are excluded.

Evidence includes calls to `stdnum.isrc.validate` or `stdnum.isrc.is_valid` through supported imports, and calls to explicitly named generic routes. Local shadows are excluded. Static matching cannot judge intent; dead code counts. Unsupported alias chains may be missed. Each route must occur in one module. Denial recognition depends on the listed wording.

## Differentiation

This audit does not cover generic input validation.
This audit does not cover ISBN book numbers.
This audit does not cover ISSN serial numbers.
This audit does not cover IBAN bank account numbers.
This audit does not cover UUID identifiers.
This audit does not cover semantic versions.
This audit does not cover MAC hardware addresses.
This audit does not cover BIC bank identifiers.
This audit does not cover cron expression validity.
This audit does not cover cron expression descriptions.
This audit does not cover scheduled execution.
This audit does not cover calendar date validity.
This audit does not cover call timeouts.
This audit does not cover card payment processing.
This audit does not cover card detail extraction.
This audit does not cover account authentication with one-time codes or confirmation links.
This audit does not cover password verification.
This audit does not cover password hashing.
This audit does not cover password generation.
This audit does not cover PDF encryption.
This audit does not cover sending email.
This audit does not cover sending SMS messages.
This audit does not cover document data extraction.
This audit does not cover barcode decoding.
This audit does not cover email address validity and deliverability.
This audit does not cover phone number validity.
This audit does not cover password strength.
This audit does not cover JSON Schema conformance.
This audit does not cover credit card number validity.
This audit does not cover domain name validity.
This audit does not cover URL validity.
This audit does not cover IP address validity.
This audit does not cover JSON parsing.
This audit does not cover regular expression matching.
This audit does not cover URL parsing.
This audit does not cover web address fetching.
This audit does not cover DNS resolution.
This audit does not cover barcode generation from account numbers.
This audit does not cover account number extraction.
This audit does not cover vehicle number extraction.
This audit does not cover vehicle number decoding.
This audit does not cover vehicle history lookup.
This audit does not cover hexadecimal color validity.
This audit does not cover ORCID identifiers.
This audit does not cover ISNI identifiers.
This audit does not cover DOI validity and resolution.
This audit does not cover CUSIP identifiers.
This audit does not cover SEDOL identifiers.
This audit does not cover ISIN securities identifiers.
This audit does not cover security record lookup.
This audit does not cover securities identifier extraction.
This audit does not cover IMEI device identifiers.
This audit does not cover MEID device identifiers.
This audit does not cover Electronic Serial Numbers.
This audit does not cover ISMN music numbers.
This audit does not cover ISAN audiovisual numbers.
This audit does not cover GRid release identifiers.
This audit does not cover EAN barcode numbers.
This audit does not cover general serial number validity.
This audit does not cover FIGI financial instrument identifiers.
This audit does not cover financial instrument record lookup.
This audit does not cover financial instrument identifier extraction.
This audit does not cover spreadsheet reading.
This audit does not cover spreadsheet generation.
This audit does not cover word-document reading.
This audit does not cover word-document generation.
This audit does not cover presentation reading.
This audit does not cover presentation generation.
This audit does not cover PDF extraction.
This audit does not cover PDF generation.
This audit does not cover PDF merging.
This audit does not cover PDF splitting.
This audit does not cover PDF rotation.
This audit does not cover PDF form-filling.
This audit does not cover PDF watermarking.
This audit does not cover PDF redaction.
This audit does not cover PDF compression.
This audit does not cover PDF annotation.
This audit does not cover table extraction.
This audit does not cover OCR.
This audit does not cover document extraction.
This audit does not cover e-signature.
This audit does not cover screen recording.
This audit does not cover video generation.
This audit does not cover QR code generation.
This audit does not cover barcode generation.
This audit does not cover barcode scanning.
This audit does not cover audio mixing.
This audit does not cover audio generation.
This audit does not cover audio editing.
This audit does not cover source separation.
This audit does not cover speech recognition.
This audit does not cover text-to-speech.
This audit does not cover noise suppression.
This audit does not cover music generation.
This audit does not cover music transcription.

## Limitations

```text
validate isrc
```

A manual runbook step can trigger a finding.

```text
isrc validation
```

A roadmap feature can trigger a finding.

```text
isrc validator
```

A hosted page can trigger a finding.

```text
isrc check
```

A field-presence lint rule can trigger a finding.

```text
check isrc
```

A manual runbook step can trigger a finding.

```text
verify isrc
```

A visual release confirmation can trigger a finding.

```text
isrc code validation
```

A field-presence check can trigger a finding.

```text
valid isrc
```

Example output can trigger a finding.

```text
isrc is valid
```

Example output can trigger a finding.

```text
isrc is invalid
```

Example error text can trigger a finding.

```text
isrc validity
```

A configuration flag or column name can trigger a finding.

```text
isrc format validation
```

A format description can trigger a finding.

```text
validate isrc number
```

A shape-only judgement can trigger a finding.

```text
isrc number validation
```

A specification section can trigger a finding.

```text
validate isrc code
```

A manual runbook step can trigger a finding.

```text
check isrc code
```

A manual runbook step can trigger a finding.

```text
validate isrc12
```

A manual runbook step can trigger a finding.

```text
isrc12 validation
```

A specification section can trigger a finding.

```text
isrc number check
```

A cataloguing checklist item can trigger a finding.

```text
isrc validation
```

An external upload service result can trigger a finding.

```text
isrc
```

This name alone makes no claim.

```text
isrc number
```

This name alone makes no claim.

```text
validate identifier
```

This general wording makes no recording-code claim.

```text
check digit
```

This term alone makes no recording-code claim.

```text
recording
```

This term alone makes no recording-code claim.

```text
country code
```

This term alone makes no recording-code claim.

```text
ismn
```

This other music number is not a recording-code claim.

A compact call only strips separators and changes case, so it is not evidence.

A format call only reformats a value, so it is not evidence.

An EAN call alone judges a different barcode number and is not evidence.

A Luhn call alone judges a different digit check and is not evidence.

The recording code has no check digit; shape and country alone determine the library judgement.

The library does not verify registration or recording existence.

The library accepts lowercase input and surrounding whitespace.

The library accepts spaces and hyphens anywhere as separators.

Regular expressions alone are not evidence.

A length check alone is not evidence.

Country membership alone is not evidence.

A lookup alone is not evidence.

An isbn call alone is not evidence.

An issn call alone is not evidence.

An ismn call alone is not evidence.

An isan call alone is not evidence.

An isin call alone is not evidence.

A validators call alone is not evidence.

A bare import, string, filename, extension, comment, or name reference is not evidence.

A subprocess invocation is not evidence.

A roadmap, changelog or todo in scanned prose still counts as a claim.

A denial outside the listed phrases may be missed.

A document outside the root readme and docs directories is not scanned.

Evidence split across modules is missed.

A local definition shadows the corresponding route name.

Dead code counts as evidence.

Alias chains that cannot be resolved are missed.

Matching is static and exact, not semantic.
