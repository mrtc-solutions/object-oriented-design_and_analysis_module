"""
PDF engine — brand-styled module document builder, parameterized by week.
Week content modules call build(cfg, story_builder).
"""
import os
import re
from PIL import Image as PILImage

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Image, Table, TableStyle, PageBreak,
                                NextPageTemplate, HRFlowable)
from reportlab.platypus.tableofcontents import TableOfContents

from common import (ROOT, BRAND, VISUALS, FONTS, OUTPUT, MAROON, MAROON_DARK,
                    MAROON_SOFT, MAROON_TINT, GOLD, GOLD_LIGHT, CREAM, CREAM_2,
                    INK, GREY)

PAGE_W, PAGE_H = A4
MARGIN = 0.9 * inch
DOC_W = PAGE_W - 2 * MARGIN

# --------------------------------------------------------------------------
# fonts
# --------------------------------------------------------------------------
def _reg():
    pdfmetrics.registerFont(TTFont("Poppins", os.path.join(FONTS, "Poppins-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Poppins-SemiBold", os.path.join(FONTS, "Poppins-SemiBold.ttf")))
    pdfmetrics.registerFont(TTFont("Poppins-Bold", os.path.join(FONTS, "Poppins-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Poppins-ExtraBold", os.path.join(FONTS, "Poppins-ExtraBold.ttf")))
    pdfmetrics.registerFont(TTFont("OpenSans", os.path.join(FONTS, "OpenSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("OpenSans-SemiBold", os.path.join(FONTS, "OpenSans-SemiBold.ttf")))
    pdfmetrics.registerFont(TTFont("OpenSans-Bold", os.path.join(FONTS, "OpenSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("OpenSans-Italic", os.path.join(FONTS, "OpenSans-Italic.ttf")))
    pdfmetrics.registerFont(TTFont("Mono", os.path.join(FONTS, "DejaVuSansMono.ttf")))
    pdfmetrics.registerFontFamily("OpenSans", normal="OpenSans", bold="OpenSans-Bold",
                                  italic="OpenSans-Italic", boldItalic="OpenSans-Bold")
    pdfmetrics.registerFontFamily("Poppins", normal="Poppins", bold="Poppins-Bold",
                                  italic="Poppins", boldItalic="Poppins-Bold")

_reg()

C_MAROON, C_DARK, C_SOFT, C_GOLD, C_GOLD_L, C_INK, C_GREY, C_CREAM = (
    "#7B1113", "#59090C", "#A94442", "#C9A227", "#E4C97C", "#2B2626", "#6B6B6B", "#FAF6EC")

# --------------------------------------------------------------------------
# styles
# --------------------------------------------------------------------------
S = {}
S["body"] = ParagraphStyle("body", fontName="OpenSans", fontSize=10.5, leading=15.5,
                           textColor=C_INK, alignment=TA_JUSTIFY, spaceAfter=6)
S["bodyL"] = ParagraphStyle("bodyL", parent=S["body"], alignment=TA_LEFT)
S["bullet"] = ParagraphStyle("bullet", parent=S["bodyL"], leftIndent=14, bulletIndent=4,
                             spaceAfter=3)
S["H1"] = ParagraphStyle("H1", fontName="Poppins-Bold", fontSize=14.5, leading=19,
                         textColor=HexColor(C_CREAM), backColor=HexColor(C_MAROON),
                         borderPadding=(7, 10, 7, 10), spaceBefore=20, spaceAfter=10,
                         keepWithNext=1)
S["H2"] = ParagraphStyle("H2", fontName="Poppins-SemiBold", fontSize=12.5, leading=16,
                         textColor=C_MAROON, spaceBefore=13, spaceAfter=4, keepWithNext=1)
S["H3"] = ParagraphStyle("H3", fontName="Poppins-SemiBold", fontSize=11, leading=14,
                         textColor=C_SOFT, spaceBefore=9, spaceAfter=3, keepWithNext=1)
S["caption"] = ParagraphStyle("caption", fontName="OpenSans-Italic", fontSize=8.5,
                              leading=11, textColor=C_GREY, alignment=TA_CENTER,
                              spaceBefore=3, spaceAfter=10)
S["callout"] = ParagraphStyle("callout", parent=S["bodyL"], spaceAfter=2)
S["mono"] = ParagraphStyle("mono", fontName="Mono", fontSize=9.5, leading=13.5,
                           textColor=C_DARK, alignment=TA_LEFT, spaceAfter=6)
S["toc"] = ParagraphStyle("toc", fontName="OpenSans", fontSize=10.5, leading=17,
                          textColor=C_INK, leftIndent=6)

GOLD_RULE = HRFlowable(width="100%", thickness=1.4, color=HexColor(C_GOLD),
                       spaceBefore=0, spaceAfter=10)

# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def H1(text):
    return Paragraph(text, S["H1"])

def H2(text):
    return Paragraph(text, S["H2"])

def H3(text):
    return Paragraph(text, S["H3"])

def P(text, style="body"):
    return Paragraph(text, S[style])

def BUL(items):
    return [Paragraph(f"<bullet>&bull;</bullet>{i}", S["bullet"]) for i in items]

def CAP(text):
    return Paragraph(text, S["caption"])

def _img(name, width):
    path = os.path.join(VISUALS, name)
    with PILImage.open(path) as im:
        w_px, h_px = im.size
    height = width * h_px / w_px
    img = Image(path, width=width, height=height)
    img.hAlign = "CENTER"
    return img

def FIG(name, caption=None, width=DOC_W):
    if caption:
        return [_img(name, width), CAP(caption)]
    return [_img(name, width)]

def CALLOUT(title, body_lines, bg=HexColor("#F3E4E4"), bar=C_GOLD, tcol=C_MAROON):
    inner = [Paragraph(f'<font name="Poppins-SemiBold" size="9" color="{tcol}">{title}</font>', S["bodyL"])]
    for line in body_lines:
        inner.append(Paragraph(line, S["callout"]))
    t = Table([[inner]], colWidths=[DOC_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 3, HexColor(bar)),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return t

def DTABLE(headers, rows, widths=None):
    if widths is None:
        widths = [DOC_W / len(headers)] * len(headers)
    hcell = [Paragraph(f'<font name="Poppins-SemiBold" size="9.5" color="{C_CREAM}">{h}</font>', S["bodyL"]) for h in headers]
    data = [hcell]
    for r in rows:
        data.append([Paragraph(f'<font name="OpenSans" size="9.5" color="{C_INK}">{c}</font>', S["bodyL"]) for c in r])
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), HexColor(C_MAROON)),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#E3D8C8")),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), HexColor(CREAM_2)))
    t.setStyle(TableStyle(style))
    return t

# --------------------------------------------------------------------------
# NumberedCanvas (Page X of Y)
# --------------------------------------------------------------------------
from reportlab.pdfgen import canvas as _canvas_mod

class NumberedCanvas(_canvas_mod.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved = []

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved)
        for state in self._saved:
            self.__dict__.update(state)
            self._draw_footer(total)
            super().showPage()
        super().save()

    def _draw_footer(self, total):
        self.setFont("OpenSans", 7.5)
        self.setFillColor(HexColor(C_CREAM if self._pageNumber == 1 else C_GREY))
        self.drawRightString(PAGE_W - MARGIN, 0.45 * inch, f"Page {self._pageNumber} of {total}")


# --------------------------------------------------------------------------
# document template
# --------------------------------------------------------------------------
class WeekDoc(BaseDocTemplate):
    def __init__(self, filename, cover_cb, cfg, **kw):
        super().__init__(filename, pagesize=A4, **kw)
        self._cover_cb = cover_cb
        self._cfg = cfg
        cover_frame = Frame(0, 0, PAGE_W, PAGE_H, id="cover")
        body_frame = Frame(MARGIN, MARGIN, DOC_W, PAGE_H - 2 * MARGIN, id="body",
                           leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="Cover", frames=[cover_frame], onPage=self._draw_cover),
            PageTemplate(id="Body", frames=[body_frame], onPage=self._draw_header_footer),
        ])

    def _draw_cover(self, canv, doc):
        self._cover_cb(canv)

    def _draw_header_footer(self, canv, doc):
        cfg = self._cfg
        canv.saveState()
        shield = os.path.join(BRAND, "eu_shield.png")
        canv.drawImage(shield, MARGIN, PAGE_H - 0.78 * inch, 0.42 * inch, 0.42 * inch,
                       mask="auto", preserveAspectRatio=True)
        canv.setFont("Poppins-SemiBold", 11)
        canv.setFillColor(HexColor(C_MAROON))
        canv.drawString(MARGIN + 0.52 * inch, PAGE_H - 0.60 * inch, "EXPLOITS UNIVERSITY")
        canv.setFont("OpenSans", 8)
        canv.setFillColor(HexColor(C_GREY))
        canv.drawString(MARGIN + 0.52 * inch, PAGE_H - 0.76 * inch,
                        "BICT 3202 — Object-Oriented Analysis and Design")
        canv.setFont("OpenSans-SemiBold", 8.5)
        canv.setFillColor(HexColor(C_SOFT))
        canv.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.66 * inch, f"Week {cfg['week']} of 16")
        canv.setStrokeColor(HexColor(C_GOLD))
        canv.setLineWidth(1.2)
        canv.line(MARGIN, PAGE_H - 0.90 * inch, PAGE_W - MARGIN, PAGE_H - 0.90 * inch)
        canv.setFont("OpenSans", 7.5)
        canv.setFillColor(HexColor(C_GREY))
        canv.drawString(MARGIN, 0.45 * inch,
                        "© Exploits University — BICT 3202 Object-Oriented Analysis and Design")
        canv.setStrokeColor(HexColor("#E3D8C8"))
        canv.setLineWidth(0.5)
        canv.line(MARGIN, 0.62 * inch, PAGE_W - MARGIN, 0.62 * inch)
        canv.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            st = flowable.style.name
            if st == "H1":
                text = flowable.getPlainText()
                if text.strip().lower() == "contents":
                    return
                key = "h1-" + re.sub(r"[^A-Za-z0-9]+", "-", text.strip().lower()).strip("-")
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(text, key, 0, 0)
                self.notify("TOCEntry", (0, text, self.page, key))


# --------------------------------------------------------------------------
# cover drawing (parameterized)
# --------------------------------------------------------------------------
def draw_cover(canv, cfg):
    w, h = PAGE_W, PAGE_H
    canv.setFillColor(HexColor(C_MAROON))
    canv.rect(0, 0, w, h, stroke=0, fill=1)
    canv.setFillColor(HexColor(C_DARK))
    canv.rect(0, 0, w, 1.6 * inch, stroke=0, fill=1)
    canv.setStrokeColor(HexColor(C_GOLD))
    canv.setLineWidth(2)
    canv.rect(0.42 * inch, 0.42 * inch, w - 0.84 * inch, h - 0.84 * inch, stroke=1, fill=0)
    canv.setLineWidth(0.8)
    canv.rect(0.52 * inch, 0.52 * inch, w - 1.04 * inch, h - 1.04 * inch, stroke=1, fill=0)

    seal = os.path.join(BRAND, "eu_seal.png")
    canv.drawImage(seal, w / 2 - 1.05 * inch, h - 3.55 * inch, 2.1 * inch, 2.1 * inch, mask="auto")

    canv.setFillColor(HexColor(C_GOLD_L))
    canv.setFont("Poppins-Bold", 30)
    canv.drawCentredString(w / 2, h - 4.05 * inch, "EXPLOITS UNIVERSITY")
    canv.setFont("OpenSans-SemiBold", 12.5)
    canv.setFillColor(HexColor(C_CREAM))
    canv.drawCentredString(w / 2, h - 4.48 * inch, "BSc INFORMATION COMMUNICATION AND TECHNOLOGY")

    canv.setFillColor(HexColor(C_GOLD))
    canv.setFont("Poppins-SemiBold", 15)
    canv.drawCentredString(w / 2, h - 5.05 * inch, "BICT 3202 · OBJECT-ORIENTED ANALYSIS AND DESIGN")

    canv.setFillColor(HexColor(C_CREAM))
    canv.setFont("Poppins-ExtraBold", 40)
    canv.drawCentredString(w / 2, h - 5.85 * inch, f"WEEK {cfg['week']}")
    # Wrap long assignment titles instead of clipping them at the page edges.
    title_style = ParagraphStyle("cover_title", fontName="Poppins-SemiBold",
                                 fontSize=15, leading=19, alignment=TA_CENTER,
                                 textColor=HexColor(C_CREAM))
    title = Paragraph(cfg["title"], title_style)
    title_width = w - 1.3 * inch
    _, title_height = title.wrap(title_width, 1.0 * inch)
    title.drawOn(canv, 0.65 * inch, h - 6.35 * inch - title_height + 15)

    bx, by, bw_, bh_ = 1.1 * inch, 1.95 * inch, w - 2.2 * inch, 1.75 * inch
    canv.setFillColor(HexColor(C_DARK))
    canv.setStrokeColor(HexColor(C_GOLD))
    canv.setLineWidth(1.2)
    canv.roundRect(bx, by, bw_, bh_, 10, stroke=1, fill=1)
    meta = [
        ("Programme", "BSc Information Communication and Technology"),
        ("Course Code / Year", "BICT 3202 · Year 3"),
        ("Lecturer", "Francis Fweta — ICT Lecturer"),
        ("Delivery", "2h Lecture · 1h Tutorial · 1h Practical · 10h Independent Learning"),
    ]
    yy = by + bh_ - 0.42 * inch
    for k, v in meta:
        canv.setFillColor(HexColor(C_GOLD))
        canv.setFont("Poppins-SemiBold", 9)
        canv.drawString(bx + 0.3 * inch, yy, k.upper())
        canv.setFillColor(HexColor(C_CREAM))
        value_x = bx + 2.35 * inch
        available = bx + bw_ - 0.15 * inch - value_x
        value_size = min(10, 10 * available / pdfmetrics.stringWidth(v, "OpenSans", 10))
        canv.setFont("OpenSans", value_size)
        canv.drawString(value_x, yy, v)
        yy -= 0.36 * inch

    canv.setFillColor(HexColor(C_CREAM))
    canv.setFont("OpenSans-Italic", 9.5)
    canv.drawCentredString(w / 2, by - 0.42 * inch,
                           f"Prepared by Francis Fweta  ·  Exploits University  ·  Week {cfg['week']} of 16")


# --------------------------------------------------------------------------
# build
# --------------------------------------------------------------------------
def build(cfg, story_builder):
    week = cfg["week"]
    out = os.path.join(OUTPUT, f"week{week}")
    os.makedirs(out, exist_ok=True)
    pdf_path = os.path.join(out, cfg["filename"])

    story = []
    toc = TableOfContents()
    toc.levelStyles = [S["toc"]]
    story.append(NextPageTemplate("Body"))
    story.append(PageBreak())
    story.append(H1("Contents"))
    story.append(toc)
    story.append(PageBreak())
    story += story_builder()

    doc = WeekDoc(pdf_path, lambda canv: draw_cover(canv, cfg), cfg,
                  leftMargin=MARGIN, rightMargin=MARGIN,
                  topMargin=MARGIN, bottomMargin=MARGIN,
                  title=f"BICT 3202 — OOAD Week {week}",
                  author="Francis Fweta")
    doc.multiBuild(story, canvasmaker=NumberedCanvas)
    return pdf_path
