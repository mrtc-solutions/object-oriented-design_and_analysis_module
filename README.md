# BICT 3202 — Object-Oriented Analysis and Design

Teaching materials for the third-year BSc Information Communication and Technology module at Exploits University.

## Course materials

- [`Course-Outline.md`](Course-Outline.md) — official module outline and learning outcomes.
- [`Week1.md`](Week1.md) through [`Week16.md`](Week16.md) — weekly lesson materials, tutorials, practical activities and revision. Week 15 focuses on an integrated OOAD case study; Week 16 consolidates the module and prepares students for assessment.
- [`assets/`](assets/) — university branding, fonts and weekly teaching visuals.
- [`tools/`](tools/) — document, presentation and visual builders for the weekly materials.
- [`exams/`](exams/) — two parallel end-of-semester practice papers and a separate examiner's marking guide.

## End-of-semester practice papers

| Document | Printable PDF | Editable Word | Markdown source |
| --- | --- | --- | --- |
| Paper A — Community Clinic Appointment System | [PDF](output/exams/candidates/End-Semester-Exam-Paper-A.pdf) | [DOCX](output/exams/candidates/End-Semester-Exam-Paper-A.docx) | [Source](exams/End-Semester-Exam-Paper-A.md) |
| Paper B — Campus Equipment Lending System | [PDF](output/exams/candidates/End-Semester-Exam-Paper-B.pdf) | [DOCX](output/exams/candidates/End-Semester-Exam-Paper-B.docx) | [Source](exams/End-Semester-Exam-Paper-B.md) |
| Examiner's Marking Guide — confidential | [PDF](output/exams/examiner/Examiner-Marking-Guide.pdf) | [DOCX](output/exams/examiner/Examiner-Marking-Guide.docx) | [Source](exams/Examiner-Marking-Guide.md) |

Keep the marking guide separate from candidate copies.

The papers use a proposed three-hour, 100-mark format (Question 1 compulsory for 40 marks, plus any three of four 20-mark questions). The course outline specifies that the examination contributes 60% of the module grade but does not specify the duration or paper format. Confirm those details with the Faculty before formal issue.

## Building weekly documents

From the repository root, create an environment and install the document-builder dependencies once:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Then build the generated materials for either week:

```bash
.venv/bin/python tools/build_all.py 15
.venv/bin/python tools/build_all.py 16
```

## Building examination documents

With the same environment, rebuild both papers and the marking guide:

```bash
.venv/bin/python tools/build_exam_docs.py
```

This writes candidate papers to `output/exams/candidates/` and the separate guide to `output/exams/examiner/`. Rebuild after editing a source so the distributed copies stay aligned.

All deliverables for this update are saved and tracked in Git under [`output/`](output/README.md): Week 15/16 modules (PDF), presentations (PPTX), assignments (PDF and DOCX), both exam papers (PDF and DOCX), and the separate guide (PDF and DOCX). Scratch previews and unrelated weekly builds remain ignored. The PDF, PowerPoint and assignment builders contain presentation-ready content in addition to the full weekly Markdown lessons; update the relevant builder when changing generated documents so the formats stay aligned.

## Review and regression checks

```bash
.venv/bin/python tools/validate_deliverables.py
.venv/bin/python -m unittest discover -s tests -v
```

The PR workflow rebuilds and validates the documents. The validation checks complete source-to-output content, exam/assignment mark totals, file structure, PDF page bounds, slide shape bounds, source links, and SHA-256 checksums. See [`output/QA-Report.md`](output/QA-Report.md) for the reviewed results and institutional limitations.

**Public practice material:** this repository is public. Do not use these published questions unchanged as a secure live examination. The examiner folder separates distribution copies; it is not access control.
