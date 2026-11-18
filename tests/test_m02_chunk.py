"""Milestone 2: chunk the documents. Run: pytest tests/test_m02_chunk.py"""

from pathlib import Path

import pytest

from chunker import chunk_documents, chunk_text
from loader import load_documents

ROOT = Path(__file__).resolve().parent.parent
HUNDRED_WORDS = " ".join(f"w{i}" for i in range(100))


def test_short_text_is_a_single_chunk():
    assert chunk_text("one two three", size=10, overlap=2) == ["one two three"]


def test_empty_text_has_no_chunks():
    assert chunk_text("   \n ", size=10, overlap=2) == []


def test_no_chunk_is_longer_than_size():
    chunks = chunk_text(HUNDRED_WORDS, size=30, overlap=5)
    assert all(len(chunk.split()) <= 30 for chunk in chunks)


def test_neighbouring_chunks_share_overlap_words():
    chunks = chunk_text(HUNDRED_WORDS, size=30, overlap=5)
    for first, second in zip(chunks, chunks[1:]):
        assert first.split()[-5:] == second.split()[:5]


def test_windows_start_where_expected():
    # size 40, overlap 10: chunks start at words 0, 30 and 60; the third reaches the end.
    chunks = chunk_text(HUNDRED_WORDS, size=40, overlap=10)
    assert [chunk.split()[0] for chunk in chunks] == ["w0", "w30", "w60"]
    assert chunks[-1].split()[-1] == "w99"


def test_no_word_is_lost():
    chunks = chunk_text(HUNDRED_WORDS, size=30, overlap=5)
    rebuilt = chunks[0].split()
    for chunk in chunks[1:]:
        rebuilt += chunk.split()[5:]
    assert rebuilt == HUNDRED_WORDS.split()


def test_overlap_must_be_smaller_than_size():
    with pytest.raises(ValueError):
        chunk_text(HUNDRED_WORDS, size=10, overlap=10)


def test_chunks_remember_their_document():
    documents = [{"source": "a.md", "text": HUNDRED_WORDS}, {"source": "b.md", "text": "short one"}]
    chunks = chunk_documents(documents, size=40, overlap=10)
    assert [chunk["id"] for chunk in chunks] == ["a.md#0", "a.md#1", "a.md#2", "b.md#0"]
    assert chunks[3] == {"id": "b.md#0", "source": "b.md", "text": "short one"}


def test_chunks_the_handbook():
    chunks = chunk_documents(load_documents(ROOT / "data"))
    assert len(chunks) > 5
    assert {chunk["source"] for chunk in chunks} == {
        "expenses.md", "it-security.md", "leave-policy.md", "onboarding.md", "remote-work.md",
    }
