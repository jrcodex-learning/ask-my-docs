import os


# Chapter 3: read every .txt file in a folder
def load_documents(folder):
    documents = []
    for name in sorted(os.listdir(folder)):
        if name.endswith(".txt"):
            path = os.path.join(folder, name)
            with open(path, encoding="utf-8") as file:
                text = file.read()
            documents.append({"source": name, "text": text})
    return documents


# Chapter 4: one chunk per paragraph
def split_into_chunks(documents):
    chunks = []
    for document in documents:
        for paragraph in document["text"].split("\n\n"):
            paragraph = paragraph.strip()
            if paragraph != "":
                chunks.append({"source": document["source"], "text": paragraph})
    return chunks


# Chapter 5: find the chunk that shares the most words with the question
def keyword_search(question, chunks):
    question_words = question.lower().replace("?", "").split()
    best_chunk = None
    best_score = 0
    for chunk in chunks:
        chunk_words = chunk["text"].lower().split()
        score = 0
        for word in question_words:
            if word in chunk_words:
                score = score + 1
        if score > best_score:
            best_score = score
            best_chunk = chunk
    return best_chunk
