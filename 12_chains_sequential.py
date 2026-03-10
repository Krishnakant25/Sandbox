from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

animal_facts = ChatPromptTemplate.from_messages(
    [
        ("system", "You like telling facts and you tell facts about {animal}."),
        ("human", "tell me {count} facts"),
    ]
)

translation_template = ChatPromptTemplate.from_messages(
    [
        ("system", "you are translator and convert the provided text into {language}."),
        ("human", "translate the following text into {language}:{text}"),
    ]
)

count_words = RunnableLambda(lambda X: f"the number of words are: {len(X.split())}\n{X}")
prepare_for_translation=RunnableLambda(lambda output: {"text": output, "language":"spanish"})

chain = chain = animal_facts | model | StrOutputParser() | prepare_for_translation | translation_template | model | StrOutputParser() | count_words

# Run the chain
result=chain.invoke({"animal":"cat", "count":2})

# Output
print(result)