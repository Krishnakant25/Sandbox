# Import required libraries
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano", temperature=1)

prompt = ChatPromptTemplate(
    {
        ("system", "You are a facts expert who knows facts about {animal}."), # system message defines model behavior
        ("human", "Tell me {fact_count} facts.")                              # human message defines what user asks
    }
)

# LCEL (LangChain Expression Language) uses the pipe symbol | to chain components
# Here, we are connecting prompt_template -> model -> output_parser
chain = prompt | model | StrOutputParser()

# The invoke() method runs the entire chain with given input values
response = chain.invoke({"animal":"elephant", "fact_count":3})

print(response) # Prints the model's plain text output (e.g., "Elephants are the largest land animals.")