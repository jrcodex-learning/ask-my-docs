from rag import load_documents, split_into_chunks, embed_chunks, answer

documents = load_documents("data")
chunks = split_into_chunks(documents)
chunk_vectors = embed_chunks(chunks)
print("Ready. Ask about the Brightpath Studio handbook.")

while True:
    question = input("\nYour question (press Enter to stop): ")
    if question == "":
        break
    print()
    print(answer(question, chunks, chunk_vectors))
