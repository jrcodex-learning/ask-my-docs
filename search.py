"""Milestone 3: keyword search, the first version of the "R" in RAG."""

import math
from collections import Counter

# Words so common they say nothing about what a passage is about.
STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "of", "to", "in", "on", "at", "for", "with", "by",
    "from", "is", "are", "was", "were", "be", "been", "it", "its", "this", "that", "these",
    "those", "i", "you", "your", "my", "me", "we", "our", "they", "their", "he", "she", "his",
    "her", "do", "does", "did", "how", "what", "which", "who", "when", "where", "why", "can",
    "could", "should", "would", "will", "as", "if", "not", "no", "so", "than", "too", "very",
    "about", "into", "up", "out", "any", "all", "each", "every", "there", "here", "have",
    "has", "had", "get", "gets", "must", "may",
}


def tokenize(text):
    """Lowercase words with punctuation removed and stopwords dropped."""
    words = []
    for raw in text.lower().split():
        word = "".join(ch for ch in raw if ch.isalnum())
        if word and word not in STOPWORDS:
            words.append(word)
    return words


class KeywordIndex:
    """Scores chunks against a question with TF-IDF: words that appear often in a chunk
    count more (term frequency), and words that appear in few chunks count more (inverse
    document frequency)."""

    def __init__(self, chunks):
        self.chunks = chunks
        self.counts = [Counter(tokenize(chunk["text"])) for chunk in chunks]
        chunks_with_word = Counter()
        for counts in self.counts:
            chunks_with_word.update(counts.keys())
        n = len(chunks)
        self.idf = {
            word: math.log((n + 1) / (df + 1)) + 1
            for word, df in chunks_with_word.items()
        }

    def score(self, query_words, counts):
        # A Counter returns 0 for a word it hasn't seen, so missing words add nothing.
        return sum(counts[word] * self.idf.get(word, 0) for word in query_words)

    def search(self, question, k=3):
        """The `k` best chunks for `question`, as (score, chunk) pairs, best first.
        Chunks that share no words with the question are left out."""
        query_words = tokenize(question)
        results = []
        for chunk, counts in zip(self.chunks, self.counts):
            score = self.score(query_words, counts)
            if score > 0:
                results.append((score, chunk))
        results.sort(key=lambda pair: pair[0], reverse=True)
        return results[:k]
