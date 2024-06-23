from langchain.memory import ConversationBufferMemory


def load_memory():
    memory= ConversationBufferMemory(
        memory_key= "chat_history",
        input_key= 'question',
        return_messages= True,
    )
    return memory

