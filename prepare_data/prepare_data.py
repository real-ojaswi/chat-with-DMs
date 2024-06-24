import json
import os
import argparse

from langchain_community.vectorstores.chroma import Chroma
from langchain_community.document_loaders import JSONLoader
from langchain.docstore.document import Document

from chat.embeddings import hfembeddings

def get_formatted_messages(root):
    """
    takes the directory containing chat json files, reorganizes and returns a dictionary in the following format:
    
    {messages: ['User 1': 'Message 1', 
                'User 2': 'Message 2',
                ....
                ]
        }
    
    """
    json_files= os.listdir(root)
    json_files= sorted(json_files, reverse=True)
    messages=[]
    for file in json_files:
        file_name= os.path.join('file/aa',file)
        with open(file_name, 'r') as file:
            data= json.load(file)
        messages= messages+data['messages'][::-1]

    msg_formatted= []
    for i, message_item in enumerate(messages):
        if 'content' in message_item:
            msg_formatted.append(f"{message_item['sender_name']}: {message_item['content']}")
    message_dict=dict()
    message_dict['messages']= msg_formatted
    return message_dict

def chunk_messages(messages, chunk_size=20, overlap=5):
    """
    takes the list of messages as the values of messages key from message_dict returned by get_formatted_messages and chunks
    them in the group of 20 (default) messages with overlap of 5 (default) messages between two chunks
    """
    chunks = []
    for i in range(0, len(messages), chunk_size - overlap):
        chunk = messages[i:i + chunk_size]
        joined_chunk = '\n'.join(chunk)
        chunks.append(joined_chunk)
        if len(chunk) < chunk_size:
            break  # Stop if we hit the end
    return chunks

def get_vector_db(root, chunk_size=20, overlap=5):
    print("Fetching and formatting messages...")
    message_dict = get_formatted_messages(root)
    messages = message_dict['messages']
    
    print(f"Chunking messages with chunk size {chunk_size} and overlap {overlap}...")
    chunks = chunk_messages(messages, chunk_size, overlap)
    
    doclist = []
    print(f"Processing chunks...")
    for i, chunk in enumerate(chunks, start=1):
        doc = Document(page_content=chunk)
        doclist.append(doc)

    persist_directory = 'vectordb/messages'
    print(f"Saving vector database to {persist_directory}...")
    vectordb = Chroma.from_documents(doclist, hfembeddings, persist_directory=persist_directory)
    
    print(f'Vector database has been stored in {persist_directory}')





