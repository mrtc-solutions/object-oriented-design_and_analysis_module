"""
Build all deliverables for a given week.
Usage:  python tools/build_all.py [week_number]

Week 1 uses the original builders (build_pdf / build_pptx / build_docx).
Week 2+ uses the parameterized engines with week content modules (wN_pdf / wN_pptx / wN_docx).
"""
import sys

from common import register_fonts, make_seal, make_shield, make_wordmark


def build_week(week):
    register_fonts()
    print("[1/4] Brand assets")
    make_seal()
    make_shield()
    make_wordmark()

    if week == 1:
        print("[2/4] Week 1 visuals")
        import visuals
        made = [fn() for fn in visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 1 documents")
        import build_pdf, build_pptx, build_docx
        print("     ", build_pdf.build())
        print("     ", build_pptx.build())
        print("     ", build_docx.build())
    elif week == 2:
        print("[2/4] Week 2 visuals")
        import week2_visuals
        made = [fn() for fn in week2_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 2 documents")
        import w2_pdf, w2_pptx, w2_docx
        print("     ", w2_pdf.build(w2_pdf.CFG, w2_pdf.story))
        print("     ", w2_pptx.build_pptx())
        print("     ", w2_docx.build(w2_docx.CFG, w2_docx.content))
    elif week == 3:
        print("[2/4] Week 3 visuals")
        import week3_visuals
        made = [fn() for fn in week3_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 3 documents")
        import w3_pdf, w3_pptx, w3_docx
        print("     ", w3_pdf.build(w3_pdf.CFG, w3_pdf.story))
        print("     ", w3_pptx.build_pptx())
        print("     ", w3_docx.build(w3_docx.CFG, w3_docx.content))
    elif week == 4:
        print("[2/4] Week 4 visuals")
        import week4_visuals
        made = [fn() for fn in week4_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 4 documents")
        import w4_pdf, w4_pptx, w4_docx
        print("     ", w4_pdf.build(w4_pdf.CFG, w4_pdf.story))
        print("     ", w4_pptx.build_pptx())
        print("     ", w4_docx.build(w4_docx.CFG, w4_docx.content))
    elif week == 5:
        print("[2/4] Week 5 visuals")
        import week5_visuals
        made = [fn() for fn in week5_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 5 documents")
        import w5_pdf, w5_pptx, w5_docx
        print("     ", w5_pdf.build(w5_pdf.CFG, w5_pdf.story))
        print("     ", w5_pptx.build_pptx())
        print("     ", w5_docx.build(w5_docx.CFG, w5_docx.content))
    elif week == 6:
        print("[2/4] Week 6 visuals")
        import week6_visuals
        made = [fn() for fn in week6_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 6 documents")
        import w6_pdf, w6_pptx, w6_docx
        print("     ", w6_pdf.build(w6_pdf.CFG, w6_pdf.story))
        print("     ", w6_pptx.build_pptx())
        print("     ", w6_docx.build(w6_docx.CFG, w6_docx.content))
    elif week == 7:
        print("[2/4] Week 7 visuals")
        import week7_visuals
        made = [fn() for fn in week7_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 7 documents")
        import w7_pdf, w7_pptx, w7_docx
        print("     ", w7_pdf.build(w7_pdf.CFG, w7_pdf.story))
        print("     ", w7_pptx.build_pptx())
        print("     ", w7_docx.build(w7_docx.CFG, w7_docx.content))
    elif week == 8:
        print("[2/4] Week 8 visuals")
        import week8_visuals
        made = [fn() for fn in week8_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 8 documents")
        import w8_pdf, w8_pptx, w8_docx
        print("     ", w8_pdf.build(w8_pdf.CFG, w8_pdf.story))
        print("     ", w8_pptx.build_pptx())
        print("     ", w8_docx.build(w8_docx.CFG, w8_docx.content))
    elif week == 9:
        print("[2/4] Week 9 visuals")
        import week9_visuals
        made = [fn() for fn in week9_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 9 documents")
        import w9_pdf, w9_pptx, w9_docx
        print("     ", w9_pdf.build(w9_pdf.CFG, w9_pdf.story))
        print("     ", w9_pptx.build_pptx())
        print("     ", w9_docx.build(w9_docx.CFG, w9_docx.content))
    elif week == 10:
        print("[2/4] Week 10 visuals")
        import week10_visuals
        made = [fn() for fn in week10_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 10 documents")
        import w10_pdf, w10_pptx, w10_docx
        print("     ", w10_pdf.build(w10_pdf.CFG, w10_pdf.story))
        print("     ", w10_pptx.build_pptx())
        print("     ", w10_docx.build(w10_docx.CFG, w10_docx.content))
    elif week == 11:
        print("[2/4] Week 11 visuals")
        import week11_visuals
        made = [fn() for fn in week11_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 11 documents")
        import w11_pdf, w11_pptx, w11_docx
        print("     ", w11_pdf.build(w11_pdf.CFG, w11_pdf.story))
        print("     ", w11_pptx.build_pptx())
        print("     ", w11_docx.build(w11_docx.CFG, w11_docx.content))
    elif week == 12:
        print("[2/4] Week 12 visuals")
        import week12_visuals
        made = [fn() for fn in week12_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 12 documents")
        import w12_pdf, w12_pptx, w12_docx
        print("     ", w12_pdf.build(w12_pdf.CFG, w12_pdf.story))
        print("     ", w12_pptx.build_pptx())
        print("     ", w12_docx.build(w12_docx.CFG, w12_docx.content))
    elif week == 13:
        print("[2/4] Week 13 visuals")
        import week13_visuals
        made = [fn() for fn in week13_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 13 documents")
        import w13_pdf, w13_pptx, w13_docx
        print("     ", w13_pdf.build(w13_pdf.CFG, w13_pdf.story))
        print("     ", w13_pptx.build_pptx())
        print("     ", w13_docx.build(w13_docx.CFG, w13_docx.content))
    elif week == 14:
        print("[2/4] Week 14 visuals")
        import week14_visuals
        made = [fn() for fn in week14_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 14 documents")
        import w14_pdf, w14_pptx, w14_docx
        print("     ", w14_pdf.build(w14_pdf.CFG, w14_pdf.story))
        print("     ", w14_pptx.build_pptx())
        print("     ", w14_docx.build(w14_docx.CFG, w14_docx.content))
    elif week == 15:
        print("[2/4] Week 15 visuals")
        import week15_visuals
        made = [fn() for fn in week15_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 15 documents")
        import w15_pdf, w15_pptx, w15_docx
        print("     ", w15_pdf.build(w15_pdf.CFG, w15_pdf.story))
        print("     ", w15_pptx.build_pptx())
        print("     ", w15_docx.build(w15_docx.CFG, w15_docx.content))
        import w15_assignment_pdf
        print("     ", w15_assignment_pdf.build(w15_assignment_pdf.CFG, w15_assignment_pdf.story))
    elif week == 16:
        print("[2/4] Week 16 visuals")
        import week16_visuals
        made = [fn() for fn in week16_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 16 documents")
        import w16_pdf, w16_pptx, w16_docx
        print("     ", w16_pdf.build(w16_pdf.CFG, w16_pdf.story))
        print("     ", w16_pptx.build_pptx())
        print("     ", w16_docx.build(w16_docx.CFG, w16_docx.content))
        import w16_assignment_pdf
        print("     ", w16_assignment_pdf.build(w16_assignment_pdf.CFG, w16_assignment_pdf.story))
    else:
        print(f"No content module yet for week {week}.")
        return
    print("DONE.")


if __name__ == "__main__":
    week = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    build_week(week)
