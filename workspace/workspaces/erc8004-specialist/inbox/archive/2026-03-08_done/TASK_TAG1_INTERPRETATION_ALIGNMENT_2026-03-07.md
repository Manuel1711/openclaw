# TASK — TAG1 interpretation alignment (2026-03-07)

## Context
Manual request from Manuel via Science-Chief: continue technical discussion on interpretation of `tag1`, including prior interesting points exchanged with Specialist and a referenced txt note.

## Required outputs (outbox)
Produce:
1) `outbox/ERC8004_TAG1_INTERPRETATION_ALIGNMENT_2026-03-07.md`
2) `outbox/ERC8004_TAG1_NA_BREAKDOWN_2026-03-07.md`

## Mandatory structure (for each output)
1. Method / Procedure
2. Key Results
3. Limitations / Problems
4. Confidence
5. Next Actions

## Technical requirements
- Clarify semantic meaning of `tag1` in current extraction artifacts.
- Explicitly separate NA causes:
  - `NA_raw_missing`
  - `NA_parse_error`
  - `NA_unmapped`
- Report percentages of each NA class over total feedback rows.
- Provide dual interpretation:
  - with NA included (data-quality view)
  - with NA excluded (semantic-content view)
- Add recommendations for normalization/mapping dictionary v1.

## Note on missing txt handoff
A txt file was mentioned by Manuel in chat history but is not visible in current workspace scan.
If unavailable locally, include a short section: "Missing handoff artifact" with exact filename/path needed.

## Priority
HIGH — active supervision thread.
