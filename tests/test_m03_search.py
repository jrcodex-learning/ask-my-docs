"""Milestone 3: keyword search. Run: pytest tests/test_m03_search.py"""

from pathlib import Path

import pytest

from chunker import chunk_documents
from loader import load_documents
from search import KeywordIndex, tokenize

ROOT = Path(__file__).resolve().parent.parent

PETS = [
    {"id": "a#0", "source": "a", "text": "Cats love fish and sleeping in the sun"},
    {"id": "b#0", "source": "b", "text": "Dogs love walks and playing fetch in the park"},
    {"id": "c#0", "source": "c", "text": "Both cats and dogs love their owners"},
]


def test_tokenize_lowercases_and_drops_punctuation():
    assert tokenize("Hello, World!") == ["hello", "world"]


def test_tokenize_drops_stopwords():
    assert tokenize("The cat and the hat") == ["cat", "hat"]


def test_tokenize_keeps_numbers():
    assert tokenize("24 days") == ["24", "days"]


def test_the_matching_chunk_comes_first():
    results = KeywordIndex(PETS).search("fish")
    assert results[0][1]["id"] == "a#0"


def test_results_are_score_and_chunk_pairs_best_first():
    results = KeywordIndex(PETS).search("cats dogs love")
    scores = [score for score, chunk in results]
    assert scores == sorted(scores, reverse=True)
    assert all(isinstance(chunk, dict) for score, chunk in results)


def test_no_shared_words_means_no_results():
    assert KeywordIndex(PETS).search("rocket science") == []


def test_k_limits_the_number_of_results():
    assert len(KeywordIndex(PETS).search("love", k=2)) == 2


def test_rare_words_count_more_than_common_ones():
    # "cats" is in two chunks, "park" in only one, so the park chunk should win.
    results = KeywordIndex(PETS).search("cats park")
    assert results[0][1]["id"] == "b#0"


@pytest.fixture(scope="module")
def handbook():
    return KeywordIndex(chunk_documents(load_documents(ROOT / "data")))


@pytest.mark.parametrize(
    "question, expected_source",
    [
        ("How many days of paid annual leave do I get?", "leave-policy.md"),
        ("Which days do teams spend in the studio together?", "remote-work.md"),
        ("What is the learning budget for books and courses?", "expenses.md"),
        ("Who meets me at reception on day one?", "onboarding.md"),
        ("How long must a password be?", "it-security.md"),
    ],
)
def test_handbook_questions_find_the_right_file(handbook, question, expected_source):
    best_score, best_chunk = handbook.search(question)[0]
    assert best_chunk["source"] == expected_source
