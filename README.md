# Ask My Docs

A question-answering app over your own documents, built step by step from the first line of
code: **retrieval-augmented generation (RAG)**. It starts as a search engine for a company
handbook and grows, milestone by milestone, into a chat app that answers from your documents
and shows its sources.

This repository is the starting point of the **JrCodex Projects** path *Ask My Docs*. The guide
for each milestone tells you what to build and why; this repository holds the handbook to
search and the tests that prove each milestone works.

## What's here

| Path | What it is |
|---|---|
| `data/` | The handbook of *Brightpath Studio*, a made-up company: the documents your app will answer questions about |
| `tests/` | One test file per milestone. A milestone is done when its tests pass |
| `requirements.txt` | The Python packages the project needs |

There is no code yet. You write it.

## Milestones

| # | Milestone | Done when this passes |
|---|---|---|
| 0 | Set up your tools | `pytest tests/test_m00_setup.py` |
| 1 | Load the documents | `pytest tests/test_m01_load.py` |
| 2 | Cut them into chunks | `pytest tests/test_m02_chunk.py` |
| 3 | Search with keywords | `pytest tests/test_m03_search.py` |
| 4 | Search by meaning (embeddings) | coming next |
| 5 | Store the vectors | |
| 6 | Ask the model, with sources | |
| 7 | A chat interface | |
| 8 | Is it any good? Evaluation | |
| 9 | Ship it | |
| 10 | Make it yours | |

## Stuck, or starting late?

The branch `solutions` has one tagged commit per milestone (`m00`, `m01`, …) with working code.
To compare your work with milestone 2's solution:

```bash
git diff m02 -- chunker.py
```

To start from the end of milestone 2 instead of your own code:

```bash
git checkout -b my-work m02
```
