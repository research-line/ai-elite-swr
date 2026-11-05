"""Test suite for LaTeX manuscript and PDF artifact integrity."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_manuscript_sources_exist():
    paper_a_en = REPO_ROOT / "paper_A" / "KI_Elite_v3_en.tex"
    paper_a_ger = REPO_ROOT / "paper_A" / "KI_Elite_v3_ger.tex"
    paper_b_en = REPO_ROOT / "paper_B" / "SWR_v4_en.tex"
    paper_b_ger = REPO_ROOT / "paper_B" / "SWR_v4_ger.tex"

    for p in [paper_a_en, paper_a_ger, paper_b_en, paper_b_ger]:
        assert p.exists(), f"Manuscript source {p.name} must exist"
        content = p.read_text(encoding="utf-8")
        assert len(content) > 10000, f"Manuscript {p.name} appears truncated"
        assert "\\documentclass" in content
        assert "\\begin{document}" in content
        assert "\\end{document}" in content


def test_compiled_pdfs_exist():
    pdfs = [
        REPO_ROOT / "paper_A" / "KI_Elite_v3_en.pdf",
        REPO_ROOT / "paper_A" / "KI_Elite_v3_ger.pdf",
        REPO_ROOT / "paper_A" / "KI_Elite_v3_kombi.pdf",
        REPO_ROOT / "paper_B" / "SWR_v4_en.pdf",
        REPO_ROOT / "paper_B" / "SWR_v4_ger.pdf",
        REPO_ROOT / "paper_B" / "SWR_v4_kombi.pdf",
    ]
    for pdf in pdfs:
        assert pdf.exists(), f"PDF artifact {pdf.name} must exist"
        assert pdf.stat().st_size > 50000, f"PDF artifact {pdf.name} too small"


def test_pdf_textlayer_quality():
    try:
        import fitz  # PyMuPDF
    except ImportError:
        try:
            import pypdf
            fitz = None
        except ImportError:
            return  # Skip if neither PDF library is installed in test environment

    pdfs = [
        REPO_ROOT / "paper_A" / "KI_Elite_v3_en.pdf",
        REPO_ROOT / "paper_B" / "SWR_v4_en.pdf",
    ]
    for pdf in pdfs:
        total_text = ""
        if fitz is not None:
            doc = fitz.open(str(pdf))
            for page in doc:
                total_text += page.get_text()
            doc.close()
        else:
            reader = pypdf.PdfReader(str(pdf))
            for page in reader.pages:
                total_text += page.extract_text() or ""

        assert len(total_text) > 10000, f"PDF {pdf.name} text layer too short"
        assert "\ufffd" not in total_text, f"PDF {pdf.name} contains Mojibake (\\ufffd)"
