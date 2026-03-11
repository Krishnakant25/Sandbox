from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

summary_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a movie critic."),
        ("human", "Provide a brief summary of the movie {movie_name}."),
    ]
)

def analyze_plot(plot):
    plot_template = ChatPromptTemplate(
        [
            ("system", "You are a movie critic."),
            ("human", "Analyze the plot: {plot}. What are its strengths and weaknesses?"),
        ]
)
    return plot_template.format_prompt(plot=plot)

def analyze_character(characters):
    character_template = ChatPromptTemplate(
        [
            ("system", "You are a movie critic."),
            ("human", "Analyze the characters: {characters}. What are their strengths and weaknesses?"),
        ]
    )
    return character_template.format_prompt(characters=characters)

# Combine analyses into a final verdict
def combine_verdicts(plot_analysis, character_analysis):
    return f"==============\nPlot Analysis:\n{plot_analysis}\n\nCharacter Analysis:\n{character_analysis} \n=============="

plot_branch = (RunnableLambda(lambda x: analyze_plot(x)) | model | StrOutputParser() )

character_branch = (RunnableLambda(lambda x: analyze_character(x)) | model | StrOutputParser())


chain = (
    summary_template 
    | model
    | StrOutputParser()
    | RunnableParallel(branches={"plot": plot_branch, "characters": character_branch})
    | RunnableLambda(lambda x: combine_verdicts(x["branches"]["plot"], x["branches"]["characters"]))
)

# Run the chain
result = chain.invoke({"movie_name": "Inception"})

print(result) 