# 🏦 Bank FAQ Chatbot

A smart assistant that answers banking-related questions using Google’s **Gemini API** (via MakerSuite) and semantic search powered by `sentence-transformers`. Built with **Streamlit** for a clean and interactive UI.

---

## 🚀 Demo

![image](https://github.com/user-attachments/assets/3eb068d9-96aa-4810-80d3-2e91ec2ba72c)


---

## 🧠 Features

- 🔍 Instant answers from a bank FAQs CSV file  
- 🧠 Powered by Google **Gemini API** (MakerSuite)  
- 🤖 Uses **semantic search** with `sentence-transformers`  
- 🎨 Streamlit-based interactive user interface  
- 📦 Modular structure with clean separation of logic  

---

## 📁 Project Structure

```
Gen-AI-Bank-FAQ-Bot/
│
├── app.py                 # Streamlit frontend
├── qna_engine.py          # Embedding + Gemini logic
├── bank_faq.csv           # CSV of bank questions & answers
├── requirements.txt       
├── .env                   # Holds Google API Key
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/gen-ai-bank-faq-bot.git
cd gen-ai-bank-faq-bot
```

2. **Create Virtual Environment**
```bash
python -m venv .venv
.venv\Scripts\activate     # For Windows
# or
source .venv/bin/activate  # For macOS/Linux
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Set Your API Key**

Create a `.env` file in the root directory:
```ini
GOOGLE_API_KEY=your_makersuite_api_key_here
```

5. **Run the App**
```bash
streamlit run app.py
```

---

## 🤖 How It Works

- Questions in `bank_faq.csv` are embedded using `sentence-transformers`
- User input is embedded and compared for similarity
- Closest FAQ is passed as a prompt to Gemini
- Gemini generates a natural language answer

---

## 🛠 Tech Stack

| Tool                  | Role                          |
|-----------------------|-------------------------------|
| Python                | Core logic and NLP            |
| Streamlit             | Web UI                        |
| sentence-transformers | Semantic similarity search    |
| Gemini (MakerSuite)   | LLM-based answer generation   |
| FAISS                 | Vector similarity search      |
| Pandas                | Data handling                 |

---

## 💬 Example Questions

- How to activate my debit card?  
- Do I need to register again for a renewed card?  
- What happens if I forget my PIN?  

---

## 🚧 Future Enhancements

- Chat history  
- Deploy to Streamlit Cloud / Render  
- Add PDF upload support  
- Speech-to-text using Whisper  

---

## 👨‍💻 Author

**Huzaifa Shaikh**  
B.Tech (AI & DS) | Aspiring Data Engineer 
