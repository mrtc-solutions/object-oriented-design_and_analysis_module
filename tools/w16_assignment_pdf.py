"""Week 16 PDF assignment; content shared with the Word renderer."""
from pdfengine import build
from revision_assignments import ASSIGNMENTS, pdf_story

CFG = {"week": 16, "title": "Assignment: " + ASSIGNMENTS[16]["title"],
       "filename": "Week16_Assignment_BICT3202_OOAD.pdf"}


def story():
    return pdf_story(16)


if __name__ == "__main__":
    print("Built:", build(CFG, story))
