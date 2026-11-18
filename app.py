"""Ask My Docs: ask questions about the handbook in the data folder."""

from chunker import chunk_documents
from loader import load_documents
from search import KeywordIndex


def main():
    documents = load_documents("data")
    chunks = chunk_documents(documents)
    index = KeywordIndex(chunks)
    print(f"Loaded {len(documents)} documents as {len(chunks)} chunks.")
    print("Ask a question about the handbook (press Enter on an empty line to quit).")
    while True:
        question = input("\nYou: ").strip()
        if not question:
            break
        results = index.search(question, k=3)
        if not results:
            print("No passage shares a word with that question. Try other words.")
            continue
        for score, chunk in results:
            print(f"\n[{chunk['source']}]  score {score:.2f}")
            print("  " + chunk["text"][:220] + "...")


if __name__ == "__main__":
    main()
