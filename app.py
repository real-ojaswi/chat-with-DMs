__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
import uuid
import sqlite3

from chat.chain import load_qa_chain
from sqlite.database import initialize_db, load_chat_history, save_message


# Initialize the database
initialize_db()

def main():
    st.set_page_config(page_title="Chat about Aashma", page_icon="💃")
    st.header('Chat about Aashma')

    # Generate or retrieve a unique user identifier
    if "user_id" not in st.session_state:
        st.session_state.user_id = str(uuid.uuid4())
    
    user_id = st.session_state.user_id
    chain = load_qa_chain()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello, ask me anything about Aashma!")
        ]
        # Load chat history from the database for this user
        rows = load_chat_history(user_id)
        for sender, message in rows:
            if sender == "AI":
                st.session_state.chat_history.append(AIMessage(content=message))
            elif sender == "Human":
                st.session_state.chat_history.append(HumanMessage(content=message))
    
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)
    
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""

    user_input = st.chat_input('Type your message here')

    if user_input is not None and user_input != "":
        human_message = HumanMessage(content=user_input)
        st.session_state.chat_history.append(human_message)
        save_message(user_id, "Human", user_input)
        
        with st.chat_message("Human"):
            st.markdown(user_input)
        
        ai_response = chain.invoke({'question': user_input})
        ai_message = AIMessage(content=ai_response['answer'])
        st.session_state.chat_history.append(ai_message)
        save_message(user_id, "AI", ai_response['answer'])

        with st.chat_message("AI"):
            st.markdown(ai_response['answer'])

if __name__ == '__main__':
    main()
