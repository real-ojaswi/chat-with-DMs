from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma

from chat.embeddings import hfembeddings

def load_retreiver(k=8): 
    vectordb= Chroma(persist_directory="./vectordb/messages", embedding_function=hfembeddings)
    
    search_kwargs= {
        "k": k
        }

    return vectordb.as_retriever(
        search_kwargs= search_kwargs
    )
