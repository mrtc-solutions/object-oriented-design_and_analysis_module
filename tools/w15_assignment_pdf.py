"""Week 15 PDF assignment; content shared with the Word renderer."""
from pdfengine import build
from revision_assignments import ASSIGNMENTS, pdf_story

CFG = {"week": 15, "title": "Assignment: " + ASSIGNMENTS[15]["title"],
       "filename": "Week15_Assignment_BICT3202_OOAD.pdf"}


def story():
    return pdf_story(15)


if __name__ == "__main__":
    print("Built:", build(CFG, story))
