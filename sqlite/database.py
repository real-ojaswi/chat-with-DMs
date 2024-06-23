import os
from dotenv import load_dotenv, find_dotenv
from supabase import create_client, Client
import streamlit as st

load_dotenv()
SUPABASE_URL = st.secrets['SUPABASE_URL']
SUPABASE_KEY = st.secrets['SUPABASE_KEY']

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def initialize_db():
    pass
# def initialize_db():
#     # Supabase automatically handles table creation via the UI or SQL queries executed through the Supabase SQL editor.
#     # You can still run the SQL command via Supabase client if necessary:
#     sql_query = '''
#     CREATE TABLE IF NOT EXISTS chat_history (
#         id SERIAL PRIMARY KEY,
#         user_id TEXT NOT NULL,
#         sender TEXT NOT NULL,
#         message TEXT NOT NULL,
#         timestamp TIMESTAMPTZ DEFAULT NOW()
#     );
#     '''
#     response = supabase.rpc('execute_sql', {'query': sql_query}).execute()
#     if response.error:
#         print(f"Error: {response.error.message}")
#     else:
#         print('Table initialized successfully')

def save_message(user_id, sender, message):
    data = {
        'user_id': user_id,
        'sender': sender,
        'message': message,
    }
    response = supabase.table('chat_history').insert(data).execute()
    print('Message saved!')

def load_chat_history(user_id):
    return []
    # response = supabase.table('chat_history').select('sender, message').eq('user_id', user_id).order('timestamp').execute()
    # return response.data
    
if __name__ == "__main__":
    # Initialize chat history table manually via Supabase dashboard before running this script
    save_message('user1', 'Alice', 'Hello, World!')
    history = load_chat_history('user1')
    for sender, message in history:
        print(f"{sender}: {message}")

