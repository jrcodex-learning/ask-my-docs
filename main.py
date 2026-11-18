from rag import load_documents, split_into_chunks, keyword_search

documents = load_documents("data")
chunks = split_into_chunks(documents)
print("Loaded", len(documents), "documents and made", len(chunks), "chunks")

while True:
    question = input("\nYour question (press Enter to stop): ")
    if question == "":
        break
    chunk = keyword_search(question, chunks)
    if chunk is None:
        print("No chunk shares a word with that question.")
    else:
        print("From", chunk["source"])
        print(chunk["text"])
