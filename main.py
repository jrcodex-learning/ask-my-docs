from rag import load_documents, split_into_chunks, embed_chunks, search

documents = load_documents("data")
chunks = split_into_chunks(documents)
chunk_vectors = embed_chunks(chunks)
print("Loaded", len(documents), "documents and made", len(chunks), "chunks")

while True:
    question = input("\nYour question (press Enter to stop): ")
    if question == "":
        break
    for chunk in search(question, chunks, chunk_vectors):
        print()
        print("From", chunk["source"])
        print(chunk["text"])
