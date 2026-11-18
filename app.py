"""Ask My Docs: ask questions about the handbook in the data folder."""

from loader import load_documents


def main():
    documents = load_documents("data")
    print(f"Loaded {len(documents)} documents:")
    for document in documents:
        words = len(document["text"].split())
        print(f"  {document['source']:<18} {words} words")


if __name__ == "__main__":
    main()
