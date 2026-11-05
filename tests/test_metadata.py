"""Test suite for repository metadata, citation, and configuration."""

import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_pyproject_toml():
    pyproject_path = REPO_ROOT / "pyproject.toml"
    assert pyproject_path.exists(), "pyproject.toml must exist"
    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)

    project = data.get("project", {})
    assert project.get("name") == "ai-elite-swr"
    assert "version" in project
    assert project.get("requires-python") == ">=3.10"
    assert project.get("license", {}).get("text") == "CC-BY-4.0"
    urls = project.get("urls", {})
    assert "Homepage" in urls
    assert "Paper A DOI" in urls
    assert "Paper B DOI" in urls


def test_citation_cff():
    citation_path = REPO_ROOT / "CITATION.cff"
    assert citation_path.exists(), "CITATION.cff must exist"
    content = citation_path.read_text(encoding="utf-8")
    assert "cff-version:" in content
    assert "Synthetic Worldview Reconstruction" in content
    assert "10.5281/zenodo.18736737" in content
    assert "10.5281/zenodo.18736720" in content
    assert "family-names: Geiger" in content
    assert "given-names: Lukas" in content


def test_llms_txt():
    llms_path = REPO_ROOT / "llms.txt"
    assert llms_path.exists(), "llms.txt must exist"
    content = llms_path.read_text(encoding="utf-8")
    assert "Synthetic Worldview Reconstruction" in content
    assert "ai-elite-swr" in content


def test_readme_structure():
    readme_path = REPO_ROOT / "README.md"
    assert readme_path.exists(), "README.md must exist"
    content = readme_path.read_text(encoding="utf-8")
    assert "Paper A" in content
    assert "Paper B" in content
    assert "NACHTRAG" in content or "Nachtrag" in content
    assert "License" in content
    assert "CC-BY 4.0" in content
