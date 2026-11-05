from __future__ import annotations

import io
from pathlib import Path
import fitz
import pypdf

ROOT = Path(__file__).resolve().parent
BASE = "SWR_v4"


def build() -> Path:
    en_pdf = ROOT / f"{BASE}_en.pdf"
    ger_pdf = ROOT / f"{BASE}_ger.pdf"
    kombi_pdf = ROOT / f"{BASE}_kombi.pdf"

    for pdf in (en_pdf, ger_pdf):
        if not pdf.exists():
            raise FileNotFoundError(f"Missing input PDF: {pdf}")

    # 1. Merge using pypdf to preserve all internal and external link annotations (/Annots)
    writer = pypdf.PdfWriter()
    writer.append(str(en_pdf))
    writer.append(str(ger_pdf))

    writer.add_metadata({
        "/Title": "Synthetic Worldview Reconstruction: A Method for LLM-Assisted Group-Level Belief System Analysis / Eine Methode zur LLM-gestützten Analyse kollektiver Glaubenssysteme auf Gruppenebene (Bilingual Edition)",
        "/Author": "Lukas Geiger",
        "/Subject": "Computational Social Science: Methodological Framework (SWR)",
        "/Keywords": "synthetic worldview reconstruction, LLM-assisted methodology, collective belief systems, ideal type, group-level analysis, computational social science, inter-instance reliability, Synthetic Worldview Reconstruction, kollektive Glaubenssysteme",
    })

    pdf_buffer = io.BytesIO()
    writer.write(pdf_buffer)
    pdf_buffer.seek(0)

    # 2. Open merged PDF in PyMuPDF to extract original TOCs and build two-part outline
    doc_en = fitz.open(str(en_pdf))
    doc_ger = fitz.open(str(ger_pdf))

    toc_en = doc_en.get_toc()
    toc_ger = doc_ger.get_toc()
    en_page_count = len(doc_en)

    combined_toc = []
    combined_toc.append([1, "Part I: English Version (Original Manuscript)", 1])
    for lvl, title, page in toc_en:
        combined_toc.append([lvl + 1, title, page])

    combined_toc.append([1, "Teil II: Deutsche Fassung (Übersetzung)", en_page_count + 1])
    for lvl, title, page in toc_ger:
        combined_toc.append([lvl + 1, title, page + en_page_count])

    doc_kombi = fitz.open(stream=pdf_buffer.getvalue(), filetype="pdf")
    total_pages = len(doc_kombi)

    doc_kombi.set_toc(combined_toc)
    doc_kombi.set_metadata({
        "title": "Synthetic Worldview Reconstruction: A Method for LLM-Assisted Group-Level Belief System Analysis / Eine Methode zur LLM-gestützten Analyse kollektiver Glaubenssysteme auf Gruppenebene (Bilingual Edition)",
        "author": "Lukas Geiger",
        "subject": "Computational Social Science: Methodological Framework (SWR)",
        "keywords": "synthetic worldview reconstruction, LLM-assisted methodology, collective belief systems, ideal type, group-level analysis, computational social science, inter-instance reliability, Synthetic Worldview Reconstruction, kollektive Glaubenssysteme",
    })

    doc_kombi.save(str(kombi_pdf), garbage=3, deflate=True)

    # Verify link counts
    total_links = sum(len(p.get_links()) for p in doc_kombi)

    doc_kombi.close()
    doc_en.close()
    doc_ger.close()

    print(
        f"Bilingual kombi PDF generated: {kombi_pdf.name} "
        f"({total_pages} pages, {kombi_pdf.stat().st_size} bytes, "
        f"{len(combined_toc)} bookmarks, {total_links} preserved hyperlinks)"
    )
    return kombi_pdf


def main() -> None:
    build()


if __name__ == "__main__":
    main()
