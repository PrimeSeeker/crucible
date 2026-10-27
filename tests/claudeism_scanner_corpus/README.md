# Claude-ism scanner corpus

Fixed inputs for `tests/test_claudeism_scanner.py`. Nothing here is shipped
prose: these files exist to be scanned.

- `pre-adaptation-bf4b26c/` — byte-exact copies of three shared workflow
  files as they stood before their host-specific constructions were removed.
  Their repo-relative paths under that directory are the locations they
  stand for, and their line numbers are the pre-adaptation ones, so the
  four happy-path positives can be asserted at the exact lines they
  occupied (35, 66, 103, 12). Copies rather than live reads by design: the
  live tree no longer carries these constructions, which is the point.
- `edge/` — one file per edge construction the scanner must catch.
- `negative/` — text that must scan clean.

Locations are bound to files by `CORPUS_LOCATIONS` in the test module.
