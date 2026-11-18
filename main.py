from rag import load_documents, split_into_chunks

documents = load_documents("data")
chunks = split_into_chunks(documents)
print("Loaded", len(documents), "documents and made", len(chunks), "chunks")

for chunk in chunks[:3]:
    print()
    print("From", chunk["source"])
    print(chunk["text"])
