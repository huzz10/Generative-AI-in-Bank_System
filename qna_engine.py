import pandas as pd
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import json
from datetime import datetime
from config import *

load_dotenv()

class BankChatbot:
    def __init__(self):
        # Validate configuration
        validate_config()
        
        # Initialize the LLM
        self.llm = ChatGoogleGenerativeAI(
            model=AI_MODEL,
            google_api_key=GOOGLE_API_KEY,
            temperature=AI_TEMPERATURE
        )
        
        # Initialize embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={'device': 'cpu'}
        )
        
        # Load FAQ data
        self.df = pd.read_csv(FAQ_FILE)
        
        # Create documents from FAQ data
        self.documents = []
        for _, row in self.df.iterrows():
            doc = Document(
                page_content=f"Question: {row['Question']}\nAnswer: {row['Answer']}",
                metadata={
                    "question": row['Question'],
                    "answer": row['Answer'],
                    "source": "bank_faq"
                }
            )
            self.documents.append(doc)
        
        # Create vector store
        self.vectorstore = Chroma.from_documents(
            documents=self.documents,
            embedding=self.embeddings,
            persist_directory=VECTOR_DB_PERSIST_DIR
        )
        
        # Initialize memory for conversation history
        self.memory = ConversationBufferWindowMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer",
            k=MEMORY_WINDOW_SIZE  # Keep last N exchanges
        )
        
        # Create conversational chain
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": RETRIEVAL_K}),
            memory=self.memory,
            return_source_documents=True,
            output_key="answer",
            verbose=False
        )
        
        # Conversation history storage
        self.conversation_history = []
        
    def get_answer(self, user_question, user_id="default"):
        """Get answer with conversation history context"""
        try:
            # Get response from the chain
            result = self.qa_chain.invoke({"question": user_question})
            
            # Handle different possible response formats
            if isinstance(result, dict):
                answer = result.get('answer', '')
                source_docs = result.get('source_documents', [])
            else:
                # If result is a string, use it as the answer
                answer = str(result)
                source_docs = []
            
            # Store conversation in history
            conversation_entry = {
                "timestamp": datetime.now().isoformat(),
                "user_id": user_id,
                "question": user_question,
                "answer": answer,
                "sources": [doc.metadata for doc in source_docs] if source_docs else []
            }
            
            self.conversation_history.append(conversation_entry)
            
            # Save conversation history to file
            self.save_conversation_history()
            
            return {
                "answer": answer,
                "sources": [doc.metadata for doc in source_docs] if source_docs else [],
                "conversation_id": len(self.conversation_history)
            }
            
        except Exception as e:
            print(f"Error in get_answer: {str(e)}")
            return {
                "answer": f"I apologize, but I encountered an error: {str(e)}",
                "sources": [],
                "conversation_id": len(self.conversation_history)
            }
    
    def get_conversation_history(self, user_id="default", limit=10):
        """Get conversation history for a specific user"""
        user_history = [
            conv for conv in self.conversation_history 
            if conv["user_id"] == user_id
        ]
        return user_history[-limit:] if limit else user_history
    
    def clear_conversation_history(self, user_id="default"):
        """Clear conversation history for a specific user"""
        self.conversation_history = [
            conv for conv in self.conversation_history 
            if conv["user_id"] != user_id
        ]
        self.memory.clear()
        self.save_conversation_history()
    
    def save_conversation_history(self):
        """Save conversation history to JSON file"""
        try:
            with open(CONVERSATION_HISTORY_FILE, "w") as f:
                json.dump(self.conversation_history, f, indent=2)
        except Exception as e:
            print(f"Error saving conversation history: {e}")
    
    def load_conversation_history(self):
        """Load conversation history from JSON file"""
        try:
            if os.path.exists(CONVERSATION_HISTORY_FILE):
                with open(CONVERSATION_HISTORY_FILE, "r") as f:
                    self.conversation_history = json.load(f)
        except Exception as e:
            print(f"Error loading conversation history: {e}")
            self.conversation_history = []

# Initialize the chatbot
chatbot = BankChatbot()
chatbot.load_conversation_history()

def get_answer(user_question, user_id="default"):
    """Wrapper function for backward compatibility"""
    return chatbot.get_answer(user_question, user_id)

def get_conversation_history(user_id="default", limit=10):
    """Get conversation history"""
    return chatbot.get_conversation_history(user_id, limit)

def clear_conversation_history(user_id="default"):
    """Clear conversation history"""
    return chatbot.clear_conversation_history(user_id)
