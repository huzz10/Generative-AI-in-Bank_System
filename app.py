import streamlit as st
from qna_engine import get_answer

st.set_page_config(page_title="Bank FAQs Bot", page_icon="🏦")
st.title("🏦 Bank FAQ Chatbot")

user_question = st.text_input("Ask a banking-related question")

if user_question:
    with st.spinner("Thinking..."):
        answer = get_answer(user_question)
    st.markdown("### 💬 Answer")
    st.write(answer)
