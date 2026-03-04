from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

template = PromptTemplate(
    input_variables=["context","question"],
    template="""
    You are a helpfull assistant that answers questions based on the provided context.
    If the context doesn't fully answer the question, say I don't know.
    Contest: {context}
    Question: {question}"""
)

chain = template | model 

user_input = {
    "context": "The capital of India is New Delhi. It is the seat of the government of India and is known for its rich history and cultural heritage.",
    "question": "Tell me about the capital of France and compare it briefly with New Delhi."
}

response = chain.invoke(user_input)
print(response.content)