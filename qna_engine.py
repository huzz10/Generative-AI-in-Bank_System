import pandas as pd
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os

load_dotenv()

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")  # ✅ Confirmed


# Load the FAQ data
df = pd.read_csv("BankFAQs.csv")
df["combined"] = df["Question"] + " " + df["Answer"]

# Load embeddings
embedder = SentenceTransformer("all-MiniLM-L6-v2")
corpus_embeddings = embedder.encode(df["combined"].tolist(), convert_to_tensor=True)

def get_answer(user_question):
    # Embed user question
    query_embedding = embedder.encode([user_question], convert_to_tensor=True)

    # Find most similar FAQ
    similarity_scores = cosine_similarity(query_embedding, corpus_embeddings)[0]
    top_idx = similarity_scores.argmax()

    faq_context = df.iloc[top_idx]

    prompt = f"""You are a banking assistant. Based on the following FAQ, answer the user's question helpfully.

FAQ:
Q: {faq_context['Question']}
A: {faq_context['Answer']}

User question:
{user_question}
"""

    response = model.generate_content(prompt)
    return response.text.strip()
