#!/usr/bin/env python3
"""AI Color Team Audit Framework — typeset report generator (template v1.1.3).

Produce a formal A4 PDF body from your completed report content, then merge a
single-page A4 cover in front (see merge_cover.py). Edit everything marked
>>> CONTENT. Keep the design rules in README.md.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, CondPageBreak, HRFlowable)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# >>> CONFIG — fonts (adjust paths per host; macOS defaults shown)
SUP = "/System/Library/Fonts/Supplemental"
pdfmetrics.registerFont(TTFont("Serif", f"{SUP}/Times New Roman.ttf"))
pdfmetrics.registerFont(TTFont("Serif-Bold", f"{SUP}/Times New Roman Bold.ttf"))
pdfmetrics.registerFont(TTFont("Serif-Italic", f"{SUP}/Times New Roman Italic.ttf"))
registerFontFamily("Serif", normal="Serif", bold="Serif-Bold", italic="Serif-Italic")

# >>> CONFIG — palette: ONE family, low saturation, one accent. Generate your own;
# do not hand-pick by feel. These defaults are a warm-neutral example.
HEADER_FILL  = colors.HexColor("#504933")   # table headers / H1 color
ACCENT       = colors.HexColor("#368aa6")   # rules and small accents ONLY
TEXT_PRIMARY = colors.HexColor("#1c1c1a")
TEXT_MUTED   = colors.HexColor("#78766f")
STRIPE       = colors.HexColor("#eeedeb")
CARD_BG      = colors.HexColor("#e8e7e4")
BORDER       = colors.HexColor("#cfcab8")
# The five panel colors appear ONLY as the swatch column (semantic use):
COLOR_RED    = colors.HexColor("#92453e")
COLOR_BLUE   = colors.HexColor("#466a8e")
COLOR_ORANGE = colors.HexColor("#a18347")
COLOR_COPPER = colors.HexColor("#504933")
COLOR_AMBER  = colors.HexColor("#8c7e52")
COLOR_WHITE  = colors.white

PAGE_W, PAGE_H = A4
MARGIN_LR = 62
AVAIL_W = PAGE_W - 2 * MARGIN_LR

# >>> CONFIG — document identity (appears in every header/footer)
DOC_TITLE = "[Auditor] Security Audit — [Product] [version] — Color Team Report"
DOC_ID = "XXX-YYY-000"

S = {
    "h1": ParagraphStyle("H1", fontName="Serif", fontSize=19, leading=24,
                         textColor=HEADER_FILL, spaceBefore=16, spaceAfter=4),
    "body": ParagraphStyle("Body", fontName="Serif", fontSize=10.5, leading=16,
                           textColor=TEXT_PRIMARY, alignment=TA_JUSTIFY, spaceAfter=8),
    "bullet": ParagraphStyle("Bullet", fontName="Serif", fontSize=10.5, leading=15.5,
                             textColor=TEXT_PRIMARY, leftIndent=16, bulletIndent=4, spaceAfter=4),
    "quote": ParagraphStyle("Quote", fontName="Serif-Italic", fontSize=10.5, leading=16,
                            textColor=TEXT_PRIMARY, leftIndent=24, alignment=TA_JUSTIFY),
    "th": ParagraphStyle("TH", fontName="Serif", fontSize=9.5, leading=12,
                         textColor=colors.white, alignment=TA_LEFT),
    "td": ParagraphStyle("TD", fontName="Serif", fontSize=9.5, leading=13,
                         textColor=TEXT_PRIMARY, alignment=TA_LEFT),
    "tdc": ParagraphStyle("TDC", fontName="Serif", fontSize=9.5, leading=13,
                          textColor=TEXT_PRIMARY, alignment=TA_CENTER),
    "stat": ParagraphStyle("Stat", fontName="Serif", fontSize=17.5, leading=21,
                           textColor=HEADER_FILL, alignment=TA_CENTER),
    "statlbl": ParagraphStyle("StatLbl", fontName="Serif", fontSize=8, leading=10,
                              textColor=TEXT_MUTED, alignment=TA_CENTER),
    "toctitle": ParagraphStyle("TOCTitle", fontName="Serif", fontSize=19, leading=24,
                               textColor=HEADER_FILL, spaceAfter=10),
}


def table(data, ratios, header=True):
    widths = [r * AVAIL_W for r in ratios]
    t = Table(data, colWidths=widths, hAlign="CENTER", repeatRows=1 if header else 0)
    cmds = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("GRID", (0, 0), (-1, -1), 0.5, BORDER)]
    if header:
        cmds.append(("BACKGROUND", (0, 0), (-1, 0), HEADER_FILL))
        for i in range(1, len(data)):
            if i % 2 == 0:
                cmds.append(("BACKGROUND", (0, i), (-1, i), STRIPE))
    t.setStyle(TableStyle(cmds))
    return t


def callout_row(stats):
    """Four stat boxes: [(value, label), ...] — extract your key numbers."""
    cell_w = (AVAIL_W - 3 * 10) / 4
    cells = []
    for value, label in stats:
        inner = Table([[Paragraph("<b>%s</b>" % value, S["stat"])],
                       [Paragraph(label.upper(), S["statlbl"])]], colWidths=[cell_w])
        inner.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), CARD_BG), ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
            ("TOPPADDING", (0, 0), (-1, 0), 9), ("BOTTOMPADDING", (0, 1), (-1, 1), 9),
            ("TOPPADDING", (0, 1), (-1, 1), 1), ("BOTTOMPADDING", (0, 0), (-1, 0), 1),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
        cells.append(inner)
    outer = Table([cells], colWidths=[cell_w + 7.5] * 4, hAlign="CENTER")
    outer.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                               ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return outer


def panel_table(rows):
    """rows = [(color, name, verdict, summary), ...] — the swatch column is the
    only place the five colors appear."""
    sw = 14
    data = [["", Paragraph("<b>Agent</b>", S["th"]), Paragraph("<b>Verdict</b>", S["th"]),
             Paragraph("<b>Report</b>", S["th"])]]
    for color, name, verdict, summary in rows:
        data.append(["\u00a0", Paragraph("<b>%s</b>" % name, S["td"]),
                     Paragraph(verdict, S["td"]), Paragraph(summary, S["td"])])
    t = Table(data, colWidths=[sw, 0.10 * (AVAIL_W - sw), 0.24 * (AVAIL_W - sw),
                               0.66 * (AVAIL_W - sw)], hAlign="CENTER", repeatRows=1)
    cmds = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
            ("BACKGROUND", (0, 0), (-1, 0), HEADER_FILL)]
    for i, (color, _, _, _) in enumerate(rows, start=1):
        cmds.append(("BACKGROUND", (0, i), (0, i), color))
        cmds.append(("BOX", (0, i), (0, i), 0.8, BORDER))
        if i % 2 == 0:
            cmds.append(("BACKGROUND", (1, i), (-1, i), STRIPE))
    t.setStyle(TableStyle(cmds))
    return t


def P(text, style="td"):
    return Paragraph(text, S[style])


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Serif", 7.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(MARGIN_LR, PAGE_H - 42, DOC_TITLE.upper())
    canvas.drawRightString(PAGE_W - MARGIN_LR, PAGE_H - 42, "PUBLIC RELEASE")
    canvas.setStrokeColor(ACCENT); canvas.setLineWidth(1.1)
    canvas.line(MARGIN_LR, PAGE_H - 48, PAGE_W - MARGIN_LR, PAGE_H - 48)
    canvas.setStrokeColor(BORDER); canvas.setLineWidth(0.5)
    canvas.line(MARGIN_LR, 44, PAGE_W - MARGIN_LR, 44)
    canvas.drawString(MARGIN_LR, 33, "DOC %s" % DOC_ID)
    canvas.drawRightString(PAGE_W - MARGIN_LR, 33, "PAGE %d" % doc.page)
    canvas.restoreState()


story = []

# >>> CONTENT — build your sections here. Shape:
# story.append(Paragraph("<b>Contents</b>", S["toctitle"]))  [if using a TOC class]
#   Document Control table (title, subject, version examined, auditor, GRADE, classification)
#   The Grade section: verdict + callout_row(stats) + the finding that holds the grade (if any)
#   The Four Questions table (Question | Verdict)
#   The Prior Findings ledger (bullets or table)
#   panel_table([...]) with the six rows
#   What This Audit Did Not Do (bullets)
#   Appendix ledger table (ID | Severity | Finding)
#   Closing attestation in S["quote"]
# Reuse table() with proportional ratios; every cell a Paragraph; keep bodies under
# ~8 pages. See REPORT-TEMPLATE.md for the content shape.

# Example skeleton (replace wholesale):
story.append(Paragraph("<b>The Grade</b>", S["h1"]))
story.append(HRFlowable(width="100%", thickness=1.1, color=ACCENT, spaceBefore=1, spaceAfter=10))
story.append(Paragraph("[One paragraph: the grade and why — if not CLEARED, the finding "
                       "that holds it and the exact path to CLEARED.]", S["body"]))
story.append(Spacer(1, 4))
story.append(callout_row([("N", "stat one"), ("N", "stat two"),
                          ("N", "stat three"), ("N", "stat four")]))
story.append(Spacer(1, 12))
story.append(panel_table([
    (COLOR_RED, "Red", "[sub-verdict]", "[2-3 sentence summary]"),
    (COLOR_BLUE, "Blue", "[sub-verdict]", "[summary]"),
    (COLOR_ORANGE, "Orange", "[sub-verdict]", "[summary]"),
    (COLOR_COPPER, "Copper", "[sub-verdict]", "[summary]"),
    (COLOR_AMBER, "Amber", "[sub-verdict]", "[summary]"),
    (COLOR_WHITE, "White", "[the gate]", "[summary]"),
]))

OUT = "body.pdf"
doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=MARGIN_LR, rightMargin=MARGIN_LR,
                        topMargin=68, bottomMargin=60, title=DOC_TITLE,
                        author="[Auditor]", creator="[Auditor]",
                        subject="[One-line subject]")
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print("body built:", doc.page, "pages")
