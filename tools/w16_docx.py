"""Week 16 Word assignment; content shared with the PDF renderer."""
from docxengine import build
from revision_assignments import ASSIGNMENTS, docx_content

CFG = {"week": 16, "title": ASSIGNMENTS[16]["title"],
       "filename": "Week16_Assignment_BICT3202_OOAD.docx"}


def content(doc, helpers):
    docx_content(16, doc, helpers)


if __name__ == "__main__":
    print("Built:", build(CFG, content))
