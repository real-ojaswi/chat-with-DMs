from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
    MessagesPlaceholder
)


def load_prompt():
    prompt= ChatPromptTemplate(
                messages=[
                    SystemMessagePromptTemplate.from_template(
                        """You are an AI assistant who has information about the chat messages between two users. Provide 
                        answer to the question based on the context provided. Things might not be explicitly expressed in message,
                        please try to make appropriate deductions as long as the deductions don't negatively affect the relationship. 
                        {context}
                        """),
                    HumanMessagePromptTemplate.from_template("question: {question}"),
                    
                ]
            )
    return prompt