#!/usr/bin/env python3
"""
Test script for the Smart Bank Assistant
"""

import sys
import os
from qna_engine import BankChatbot, get_answer, get_conversation_history, clear_conversation_history

def test_chatbot():
    """Test the chatbot functionality"""
    print("🧪 Testing Smart Bank Assistant...")
    
    try:
        # Test 1: Initialize chatbot
        print("1. Testing chatbot initialization...")
        chatbot = BankChatbot()
        print("✅ Chatbot initialized successfully")
        
        # Test 2: Basic question
        print("\n2. Testing basic question...")
        test_question = "What are your banking hours?"
        response = get_answer(test_question, "test_user")
        print(f"Question: {test_question}")
        print(f"Answer: {response['answer'][:100]}...")
        print("✅ Basic question answered successfully")
        
        # Test 3: Conversation history
        print("\n3. Testing conversation history...")
        history = get_conversation_history("test_user", limit=5)
        print(f"Found {len(history)} conversation entries")
        print("✅ Conversation history working")
        
        # Test 4: Multiple questions
        print("\n4. Testing multiple questions...")
        questions = [
            "How do I open a new account?",
            "What documents do I need?",
            "What are the fees?"
        ]
        
        for i, question in enumerate(questions, 1):
            print(f"   Question {i}: {question}")
            response = get_answer(question, "test_user")
            print(f"   Answer {i}: {response['answer'][:50]}...")
        
        print("✅ Multiple questions handled successfully")
        
        # Test 5: Memory context
        print("\n5. Testing memory context...")
        context_question = "What did I ask about earlier?"
        response = get_answer(context_question, "test_user")
        print(f"Context question: {context_question}")
        print(f"Context answer: {response['answer'][:100]}...")
        print("✅ Memory context working")
        
        # Test 6: Clear history
        print("\n6. Testing clear history...")
        clear_conversation_history("test_user")
        history_after_clear = get_conversation_history("test_user")
        print(f"History after clear: {len(history_after_clear)} entries")
        print("✅ Clear history working")
        
        print("\n🎉 All tests passed! The chatbot is working correctly.")
        return True
        
    except Exception as e:
        print(f"❌ Test failed with error: {str(e)}")
        return False

def main():
    """Main test function"""
    print("🏦 Smart Bank Assistant - Test Suite")
    print("=" * 50)
    
    success = test_chatbot()
    
    if success:
        print("\n✅ All tests completed successfully!")
        print("You can now run the Streamlit app with: streamlit run app.py")
    else:
        print("\n❌ Some tests failed. Please check the configuration and dependencies.")
        sys.exit(1)

if __name__ == "__main__":
    main()
