## Conversational chatbot using Gemini API

import os
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Gemini Chatbot", page_icon=":robot_face:")
st.header(" Hey there!")

chat_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # or "gemini-1.5-pro"
    google_api_key="AIzaSyCZ891oZE6NikETOruri49t82OFUp4PoVU"
)


if 'flowmessages' not in st.session_state:
   st.session_state['flowmessages']=[
       SystemMessage(content="You are a helpful assistant that can answer questions and help with tasks.")
   ]
 #Function to load the gemini modle and get respone
def get_chatmodel_response(question): 
        st.session_state['flowmessages'].append(HumanMessage(content=question))
        answer=chat_model(st.session_state['flowmessages'])
        st.session_state['flowmessages'].append(AIMessage(content=answer.content))
        return answer.content
    
input = st.text_input("Input:" , key="input")
response = get_chatmodel_response(input)

submit = st.button("Ask the question")

###If ask buttonn is clicked

if submit:
    st.subheader("Answer:")
    st.write(response)









