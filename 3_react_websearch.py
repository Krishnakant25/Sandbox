from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.agents import AgentExecutor, tool, create_react_agent
from langchain_classic import hub
from duckduckgo_search import DDGS

load_dotenv()

model = ChatOpenAI(model="gpt-4")

@tool
def web_search_tool(query: str, max_results: int= 3):
    """
    Search the web using DuckDuckGo and return the top results.
    
    Parameters:
        query (str): The user’s search query.
        max_results (int): Number of top results to return (default = 3).
        
    Returns:
        str: A formatted string containing the titles and snippets of the results.
    
    Explanation:
        - This function is decorated with @tool, making it a callable tool for the agent.
        - The LLM can decide to call this tool when it needs real-time information.
    """

    with DDGS() as ddg:
        result = ddg.text(query, max_results=max_results)
        return "\n".join([f"{r['title'] | r['body']}" for r in result])
    
tools = [web_search_tool]

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm=model, prompt=prompt, tools=tools)

agent_exec = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = "Who is the current Prime Minister of Canada?"
# You can replace this query with any topic — it will use web_search automatically.

result = agent_exec.invoke({"input": query})
# invoke(): sends the query to the agent → agent decides what to do → executes tools → returns final answer.

print("\n✅ FINAL ANSWER:")
print(result["output"])