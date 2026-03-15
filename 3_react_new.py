from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from duckduckgo_search import DDGS

from langchain.tools import tool
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Model
model = ChatOpenAI(model="gpt-4o", temperature=0)

# Tool
@tool
def web_search(query: str, max_results: int = 3) -> str:
    """Search the web using DuckDuckGo"""
    
    with DDGS() as ddg:
        results = ddg.text(query, max_results=max_results)

    return "\n".join(
        f"{r['title']}: {r['body']}" for r in results
    )


tools = [web_search]

# Local ReAct prompt
template = """
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use this format:

Question: the input question
Thought: think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (repeat if needed)
Thought: I now know the final answer
Final Answer: the answer

Question: {input}
{agent_scratchpad}
"""

prompt = PromptTemplate.from_template(template)

# Create agent
agent = create_react_agent(model, tools, prompt)

# Executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = "Who is the current Prime Minister of Canada?"

result = agent_executor.invoke({"input": query})

print("\n✅ FINAL ANSWER:")
print(result["output"])