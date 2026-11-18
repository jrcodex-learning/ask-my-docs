"""Milestone 1: load the documents. Run: pytest tests/test_m01_load.py"""

from pathlib import Path

from loader import clean_text, load_documents

ROOT = Path(__file__).resolve().parent.parent


def test_clean_text_makes_all_line_endings_the_same():
    assert clean_text("a\r\nb\rc") == "a\nb\nc"


def test_clean_text_removes_spaces_at_line_ends():
    assert clean_text("hello   \nworld\t") == "hello\nworld"


def test_clean_text_keeps_paragraphs_but_squeezes_big_gaps():
    assert clean_text("first\n\nsecond") == "first\n\nsecond"
    assert clean_text("first\n\n\n\n\nsecond") == "first\n\nsecond"


def test_clean_text_trims_the_ends():
    assert clean_text("\n\n  hi there  \n\n") == "hi there"


def test_reads_only_md_and_txt_files(tmp_path):
    (tmp_path / "a.md").write_text("alpha", encoding="utf-8")
    (tmp_path / "b.txt").write_text("beta", encoding="utf-8")
    (tmp_path / "c.tmp").write_text("not a document", encoding="utf-8")
    (tmp_path / "d.py").write_text("print(1)", encoding="utf-8")
    sources = [doc["source"] for doc in load_documents(tmp_path)]
    assert sources == ["a.md", "b.txt"]


def test_skips_empty_files(tmp_path):
    (tmp_path / "empty.md").write_text("", encoding="utf-8")
    (tmp_path / "blank.md").write_text("   \n\n  ", encoding="utf-8")
    assert load_documents(tmp_path) == []


def test_each_document_has_its_source_and_clean_text(tmp_path):
    (tmp_path / "policy.md").write_text("Line one   \r\n\r\n\r\nLine two\r\n", encoding="utf-8")
    assert load_documents(tmp_path) == [{"source": "policy.md", "text": "Line one\n\nLine two"}]


def test_documents_come_back_sorted_by_name(tmp_path):
    for name in ["zebra.md", "apple.md", "mango.txt"]:
        (tmp_path / name).write_text(name, encoding="utf-8")
    assert [doc["source"] for doc in load_documents(tmp_path)] == ["apple.md", "mango.txt", "zebra.md"]


def test_loads_the_handbook():
    documents = load_documents(ROOT / "data")
    assert len(documents) == 5
    assert all(doc["text"].startswith("# ") for doc in documents)
