from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "How much time off do I get?",
    "Everyone gets 24 days of paid annual leave each year.",
    "Lock your laptop screen when you walk away.",
]

vectors = model.encode(sentences)
print("Each sentence became", len(vectors[0]), "numbers")
print("The first five numbers of sentence 1:", vectors[0][:5])

scores = model.similarity(vectors[0], vectors)
print()
for i in range(len(sentences)):
    print(round(float(scores[0][i]), 2), sentences[i])
