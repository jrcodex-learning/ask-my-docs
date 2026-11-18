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
