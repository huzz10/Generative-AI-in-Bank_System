import streamlit as st
from qna_engine import get_answer

st.set_page_config(page_title="Bank FAQs Bot", page_icon="🏦", layout="centered")
st.title("🏦 Welcome to Your Bank FAQ Assistant")
st.markdown("Ask any question related to banking and I’ll help you with instant answers.")

# Store input in session_state
if "question" not in st.session_state:
    st.session_state.question = ""
if "answer" not in st.session_state:
    st.session_state.answer = ""

# Input
user_question = st.text_input("💬 What would you like to know?", key="input_question")

# Button to submit
if st.button("Ask"):
    if user_question.strip():
        st.session_state.question = user_question.strip()
        with st.spinner("🤖 Thinking..."):
            st.session_state.answer = get_answer(user_question.strip())

# Display Q&A
if st.session_state.answer:
    st.markdown("### 📝 **Question**")
    st.markdown(f"> {st.session_state.question}")
    
    st.markdown("### 💡 **Answer**")
    st.markdown(st.session_state.answer)
