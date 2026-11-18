"""Ask My Docs: ask questions about the handbook in the data folder."""

from chunker import chunk_documents
from loader import load_documents


def main():
    documents = load_documents("data")
    chunks = chunk_documents(documents)
    print(f"Loaded {len(documents)} documents as {len(chunks)} chunks.")
    print("\nThe first two chunks (notice the words they share):")
    for chunk in chunks[:2]:
        print(f"\n[{chunk['id']}]")
        print("  " + chunk["text"])


if __name__ == "__main__":
    main()
