"""Positive and deliberately corrupted-input regressions for deliverable checks."""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from build_exam_docs import inline_tokens, md_table_rows, reportlab_inline
from revision_assignments import ASSIGNMENTS
from validate_deliverables import (ROOT, check_assignment_marks, check_exam_marks,
                                   check_passages, expected_files, manifest_text, validate)


class SourceRegressionTests(unittest.TestCase):
    def test_both_papers_marks(self):
        for paper in ("A", "B"):
            check_exam_marks((ROOT / f"exams/End-Semester-Exam-Paper-{paper}.md").read_text())

    def test_reject_wrong_exam_marks(self):
        text = (ROOT / "exams/End-Semester-Exam-Paper-A.md").read_text()
        with self.assertRaisesRegex(AssertionError, "marks"):
            check_exam_marks(text.replace("**[12 marks]**", "**[11 marks]**", 1))

    def test_reject_wrong_subpart_order(self):
        text = (ROOT / "exams/End-Semester-Exam-Paper-A.md").read_text()
        with self.assertRaisesRegex(AssertionError, "subpart"):
            check_exam_marks(text.replace("**(c)**", "**(z)**", 1))

    def test_assignment_totals(self):
        for data in ASSIGNMENTS.values():
            check_assignment_marks(data)

    def test_reject_assignment_original_18_mark_bug(self):
        data = copy.deepcopy(ASSIGNMENTS[15])
        data["short"][0] = (data["short"][0][0], 1)
        with self.assertRaisesRegex(AssertionError, "Section A"):
            check_assignment_marks(data)

    def test_reject_missing_content(self):
        with self.assertRaisesRegex(AssertionError, "missing content"):
            check_passages(["Loan rollback"], "Loan creation", "deliberately truncated")

    def test_nested_inline_code_and_escaping(self):
        result = reportlab_inline('**`<<include>>`** & <tag>')
        self.assertIn('<b><font name="ExamMono">&lt;&lt;include&gt;&gt;</font></b>', result)
        self.assertIn('&amp; &lt;tag&gt;', result)
        self.assertNotIn('`', result)

    def test_plain_bold_italic_tokens(self):
        self.assertEqual(list(inline_tokens('one **two** *three* `four`')),
                         [('one ', 'plain'), ('two', 'bold'), (' ', 'plain'),
                          ('three', 'italic'), (' ', 'plain'), ('four', 'code')])

    def test_table_separator_and_empty_cells(self):
        self.assertEqual(md_table_rows(['| a | |', '|---|:---:|', '| b | c |']),
                         [['a', ''], ['b', 'c']])

    def test_fourteen_deliverables_under_output(self):
        self.assertEqual(len(expected_files()), 14)
        self.assertTrue(all(p.is_relative_to(ROOT / 'output') for p in expected_files()))

    def test_saved_checksums(self):
        self.assertEqual((ROOT / 'output/checksums.sha256').read_text(), manifest_text())

    def test_entire_deliverable_suite(self):
        validate()


if __name__ == '__main__':
    unittest.main()
