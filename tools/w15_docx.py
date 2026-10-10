"""Week 15 Word assignment; content shared with the PDF renderer."""
from docxengine import build
from revision_assignments import ASSIGNMENTS, docx_content

CFG = {"week": 15, "title": ASSIGNMENTS[15]["title"],
       "filename": "Week15_Assignment_BICT3202_OOAD.docx"}


def content(doc, helpers):
    docx_content(15, doc, helpers)


if __name__ == "__main__":
    print("Built:", build(CFG, content))
