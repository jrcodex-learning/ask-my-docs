"""Milestone 2: cut documents into overlapping chunks of words."""


def chunk_text(text, size=60, overlap=15):
    """Split `text` into chunks of at most `size` words.

    Each chunk starts `size - overlap` words after the previous one, so neighbours share
    `overlap` words and no sentence is lost at a boundary.
    """
    if overlap >= size:
        raise ValueError("overlap must be smaller than size")
    words = text.split()
    if not words:
        return []
    step = size - overlap
    chunks = []
    start = 0
    while True:
        chunks.append(" ".join(words[start:start + size]))
        if start + size >= len(words):
            break  # this chunk reached the last word
        start += step
    return chunks


def chunk_documents(documents, size=60, overlap=15):
    """Chunk every document. Each chunk remembers where it came from."""
    chunks = []
    for document in documents:
        pieces = chunk_text(document["text"], size, overlap)
        for number, piece in enumerate(pieces):
            chunks.append({
                "id": f"{document['source']}#{number}",
                "source": document["source"],
                "text": piece,
            })
    return chunks
