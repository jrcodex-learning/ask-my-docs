from rag import load_documents

documents = load_documents("data")
print("Loaded", len(documents), "documents")
for document in documents:
    print("-", document["source"], len(document["text"]), "characters")
