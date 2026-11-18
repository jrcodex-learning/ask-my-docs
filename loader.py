"""Milestone 1: load the handbook from a folder of text files."""

from pathlib import Path

# The kinds of file we know how to read. Everything else in the folder is skipped.
ALLOWED_SUFFIXES = {".md", ".txt"}


def clean_text(text):
    """Tidy a document's text without changing what it says."""
    # Windows writes line endings as \r\n and old Macs as \r: make them all \n.
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # Spaces at the end of a line are invisible noise.
    lines = [line.rstrip() for line in text.split("\n")]
    text = "\n".join(lines)
    # Keep paragraphs (one blank line) but squeeze bigger gaps down to one.
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")
    return text.strip()


def load_documents(folder="data"):
    """Read every .md and .txt file in `folder`, sorted by name.

    Returns a list of documents, each a dict: {"source": file name, "text": cleaned text}.
    Empty files are skipped.
    """
    documents = []
    for path in sorted(Path(folder).iterdir()):
        if path.suffix.lower() not in ALLOWED_SUFFIXES:
            continue
        text = clean_text(path.read_text(encoding="utf-8"))
        if not text:
            continue
        documents.append({"source": path.name, "text": text})
    return documents
