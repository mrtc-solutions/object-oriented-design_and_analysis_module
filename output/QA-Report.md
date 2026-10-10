# Week 15–16 and end-of-semester deliverable review

Review date: 10 October 2026. Scope: the Week 15/16 update and two parallel BICT 3202 practice papers, not a certification of every historic file in this repository.

## Deliverable inventory

All 14 distribution documents are saved under `output/` and included in Git:

- `week15/`: module PDF, presentation PPTX, assignment PDF and DOCX.
- `week16/`: module PDF, presentation PPTX, assignment PDF and DOCX.
- `exams/candidates/`: Paper A PDF/DOCX and Paper B PDF/DOCX.
- `exams/examiner/`: separate marking guide PDF/DOCX.

Use the [output index](README.md) for download links. Only Markdown sources remain in the root `exams/` directory. Scratch previews are excluded from Git.

## Defects identified and corrected

1. Generated exams were outside `output/`, and Git ignored the weekly distribution copies. Builders now use `output/exams/candidates/` and `output/exams/examiner/`; targeted Git exceptions include the reviewed deliverables without including unrelated generated files.
2. Week 15's old PDF assignment had 18 Section A marks despite advertising 20, and the Week 15/16 PDF assignments differed from their Word versions. Both renderers now share `tools/revision_assignments.py`; each assignment is 20 + 20 + 10 = 50 marks.
3. Assignment PDF cover titles were clipped at the page edges. Titles now wrap within the cover width.
4. Several Week 15/16 slide images overlapped takeaway/footer bands; Week 15's integrated model also extended off-slide. Those weeks now fit images proportionally above the lower band without cropping.
5. Exam lifecycle questions previously forced a minimum state count that could encourage redundant Loan states. They now assess meaningful states, guards and transitions; the guide explicitly accepts a renewal-count self-transition.
6. Clarified clinic cancellation boundary (including exactly 24 elapsed hours), staff referral versus cancellation, event order, late check-in/No-show competition, and non-overlapping [start, end) intervals. Booking reservation and persistence are atomic; notification follows commit.
7. Clarified equipment-loan limit checks, Overdue counting, renewal eligibility, FIFO reservation holds, cancellation/repair behaviour, copy allocation versus queue Reservation, failed-checkout rollback, and notification after commit. The guide follows the same rules.
8. Word titles, table widths, page-field sizes and update settings were corrected. Nested inline code in bold marking-guide text renders without Markdown delimiters.
9. Replaced the historic hard-coded, destructive PDF build script with a repository-relative, non-destructive build that fails on errors instead of hiding them.
10. Added pinned tested direct dependencies, fail-closed validation, positive/negative regression tests, checksums and a PR/main rebuild workflow.

## Recorded local results

- 14/14 distribution documents passed the implemented acceptance checks.
- 12/12 regression tests passed, including corrupted-input rejection tests.
- 14/14 SHA-256 checksums matched.
- Week 15: 22-page module, 26 slides, 5-page assignment PDF plus Word.
- Week 16: 21-page module, 26 slides, 5-page assignment PDF plus Word.
- Papers A and B: 3 pages each; marking guide: 6 pages.
- Python source parsing and `git diff --check` passed.

## Automated acceptance checks

Run from the repository root:

```bash
.venv/bin/python tools/validate_deliverables.py
.venv/bin/python -m unittest discover -s tests -v
sha256sum -c output/checksums.sha256
```

The validator checks all 14 files: expected inventory, PDF readability and A4 page bounds, no clipped text or replacement glyphs, complete passage-level exam source coverage in PDF and Word, identical weekly assignment content and marks, exam subpart and question totals, candidate/examiner distribution labels, provisional-duration notice, Office ZIP/image integrity, table widths, 26-slide decks with on-slide shapes and no image/header/footer overlap, essential module sections/themes, relative download links and SHA-256 checksums.

Twelve regression tests include deliberate wrong marks, wrong subpart ordering and truncated output so the checker is tested to reject defects, not merely report a happy path. CI validates checked-in copies, rebuilds both weeks and the exams, then runs the same checks on the rebuilt copies.

## Human/institutional limits

Passing the implemented checks is not proof of universal “10/10” educational effectiveness. The Faculty must confirm the proposed three-hour duration, 100-mark paper structure, permitted materials and timetable. The course outline specifies 17 weeks while teaching files span Weeks 1–16; the approved calendar still needs confirmation. The examination contributes 60% of the final course grade; apply this weighting once to the 100 raw marks.

This repository is public. These papers are published practice forms, not secure unseen live exams. Examiner folder separation and confidential labels do not provide access control. For formal examinations, moderate the academic level and timing, create unseen questions, and store candidate and marking materials under institutional security controls.

PDFs were inspected visually during the review. Word and PowerPoint were checked structurally and for content/shape bounds; rendering can differ across Office versions and installed fonts. Final print proofing in the institution's Office/printer environment remains appropriate.
