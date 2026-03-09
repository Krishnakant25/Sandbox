from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableLambda
from langchain_community.chat_models import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You love facts and you tell facts about {animal}"),  # Defines AI behavior
        ("human", "Tell me {count} facts."),                             # User instruction
    ]
)

# -------------------- DEFINE INDIVIDUAL RUNNABLES (CHAIN STEPS) --------------------
# RunnableLambda is used to wrap any Python function into a "Runnable" step.

# Step 1 → Format the prompt using given input (fills placeholders with actual values)
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))

# Step 2 → Send the formatted prompt to the model and get response messages
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))

# Step 3 → Extract only the text content from the model’s response (remove metadata)
parse_output = RunnableLambda(lambda x: x.content)

# -------------------- CREATE A RUNNABLE SEQUENCE --------------------
# RunnableSequence connects the above steps one after another (like a pipeline)
chain = RunnableSequence(
    first=format_prompt,      # Step 1: Format the prompt
    middle=[invoke_model],    # Step 2: Invoke model
    last=parse_output         # Step 3: Parse output
)

# -------------------- RUN THE CHAIN --------------------
# Provide the inputs for placeholders {animal} and {count}
response = chain.invoke({"animal": "cat", "count": 2})

# -------------------- PRINT THE FINAL OUTPUT --------------------
print(response)