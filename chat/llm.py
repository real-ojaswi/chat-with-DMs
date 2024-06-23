from langchain_openai.chat_models import ChatOpenAI
# from dotenv import load_dotenv, find_dotenv
import streamlit as st
import os

# load_dotenv(find_dotenv())

os.environ['OPENAI_API_KEY']= st.secrets['OPENAI_API_KEY']

def load_llm(temperature= 0.4):
    chat= ChatOpenAI(streaming= True, temperature=0.4)
    return chat
