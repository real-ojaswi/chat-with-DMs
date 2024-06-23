from langchain.chains import ConversationalRetrievalChain

from chat.chroma_db import load_retreiver
from chat.memory import load_memory
from chat.llm import load_llm
from chat.prompt import load_prompt


def load_qa_chain(llm=None, retriever= None, memory=None, prompt=None):
    if retriever is None:
        retriever= load_retreiver()
    if memory is None:
        memory= load_memory()
    if llm is None:
        llm= load_llm()
    if prompt is None:
        prompt= load_prompt()
    
    chain= ConversationalRetrievalChain.from_llm(
        llm= llm,
        memory= memory,
        retriever= retriever,
        chain_type= 'stuff',
        verbose= True,
        combine_docs_chain_kwargs={'prompt': prompt}   
    )

    return chain