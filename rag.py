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
