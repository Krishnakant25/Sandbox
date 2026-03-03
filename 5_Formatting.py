from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

class movie(BaseModel):
    title: str = Field(description="The title of the movie")
    director: str = Field(description="The director of the movie")
    release_date: int = Field(description="Which year movie was released")
    description: str = Field(description="Brief description or summary of the movie")

model = ChatOpenAI(model="gpt-5-nano", temperature=1)

parser = PydanticOutputParser(pydantic_object=movie)

template = PromptTemplate(input_variables=["Context","Question"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
    template="""
    You are a helpful assistant that answers questions about movies.
    Use the context if available, but if the context does not fully answer, generate additional details based on general knowledge.
    Context: {context}
    Question: {question}
    Answer in JSON format:
    {format_instructions}
    """
)

chain = template | model | parser


user_input = {
    # Context is optional; here it supplies known facts to steer generation
    "context": "The movie 'Inception' is directed by Christopher Nolan and was released in 2010.",
    "question": "Give me the full details of the movie including a short summary."
}

movie_struct = chain.invoke(user_input)

print("\nStructured JSON Output:\n", movie_struct.model_dump_json(indent=2))