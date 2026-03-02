
# user_input -> template -> model -> response   #step-by-step flow

## Importing libraries
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

## Model Creation
model = ChatOpenAI(model="gpt-5-nano")

## Define a prompt template
template = PromptTemplate.from_template(
    """You are a helpful assistant that answers questions based on the provided context. If you cant
    find the answer in the context, say 'I don't know'.
    Context: {context}
    Question: {question}
    Answer:"""
)

## Generate a prompt using the template
user_input = {
    "context": "The capitall of India is New Delhi. It is the seat of the government of India and is known for its rich history and culltural heritage,",
    "question": "What is the capital of India?"
}

chain = template | model ## create a chain that combines the template and the models 

## Generate response using the chain
response = chain.invoke(user_input)

#print(response) #print the response from the model
print(response.content)