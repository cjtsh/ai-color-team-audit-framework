#!/usr/bin/env python3
"""Merge a single-page A4 cover in front of the report body -> final PDF."""
import sys
from pypdf import PdfReader, PdfWriter, Transformation

A4_W, A4_H = 595.28, 841.89


def norm(page):
    w, h = float(page.mediabox.width), float(page.mediabox.height)
    if abs(w - A4_W) > 2 or abs(h - A4_H) > 2:
        page.add_transformation(Transformation().scale(A4_W / w, A4_H / h))
        page.mediabox.lower_left = (0, 0)
        page.mediabox.upper_right = (A4_W, A4_H)
    return page


def main(body, cover, out, title):
    w = PdfWriter()
    w.add_page(norm(PdfReader(cover).pages[0]))
    for p in PdfReader(body).pages:
        w.add_page(norm(p))
    w.add_metadata({"/Title": title, "/Author": "[Auditor]", "/Creator": "[Auditor]"})
    with open(out, "wb") as f:
        w.write(f)
    print("merged:", len(PdfReader(out).pages), "pages ->", out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "Color Team Audit Report")
