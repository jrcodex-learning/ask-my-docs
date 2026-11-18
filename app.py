import streamlit as st

from rag import load_documents, split_into_chunks, embed_chunks, answer


@st.cache_resource  # do the slow work once, not for every question
def prepare():
    chunks = split_into_chunks(load_documents("data"))
    return chunks, embed_chunks(chunks)


chunks, chunk_vectors = prepare()

st.title("Ask My Docs")
st.write("Ask anything about the Brightpath Studio handbook.")

question = st.chat_input("Your question")
if question:
    st.chat_message("user").write(question)
    with st.spinner("Thinking..."):
        reply = answer(question, chunks, chunk_vectors)
    st.chat_message("assistant").write(reply)
