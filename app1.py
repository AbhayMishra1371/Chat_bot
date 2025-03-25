import os
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Streamlit UI Setup
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("💬 Gemini AI Chatbot")

# Initialize the Gemini model
chat_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # or "gemini-1.5-pro"
    google_api_key=gemini_api_key
)

# Initialize session state for storing chat messages
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]

# Function to get Gemini's response
def get_chat_response(user_input):
    """Send user input to the Gemini model and get a response."""
    st.session_state['messages'].append(HumanMessage(content=user_input))
    response = chat_model.invoke(st.session_state['messages'])
    st.session_state['messages'].append(AIMessage(content=response.content))
    return response.content

# Create chat input and display messages
user_input = st.text_input("Ask me anything:", key="input")

if st.button("Send"):
    if user_input:
        response = get_chat_response(user_input)
        st.subheader("🤖 Gemini AI says:")
        st.write(response)
    else:
        st.warning("⚠️ Please enter a question before clicking 'Send'.")

# Display the full conversation history
st.subheader("📜 Chat History")
for msg in st.session_state['messages']:
    if isinstance(msg, HumanMessage):
        st.write(f"👤 **You:** {msg.content}")
    elif isinstance(msg, AIMessage):
        st.write(f"🤖 **Gemini:** {msg.content}")
