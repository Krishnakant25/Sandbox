from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_classic.agents import create_react_agent, AgentExecutor, tool
import datetime
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """
    Returns the current system time as a string using the provided format.
    - The @tool decorator converts this function into a tool the agent can call.
    - format: a strftime format string (default "YYYY-mm-dd HH:MM:SS").
    NOTE: http://datetime.datetime.now() uses your system's local timezone.
    If you want true IST regardless of the machine location, use timezone-aware code
    (shown in the comment below).
    """
    return datetime.datetime.now().strftime(format)

custom_prompt = """
You are a helpful AI agent.

You have access to the following tools:
{tools}

You are currently running in **India Standard Time (IST)**.
If the user asks for time in another city, you must:
1. Use the 'get_system_time' tool to fetch the current IST time.
2. Convert the time to the requested city by applying the timezone difference manually.

Use the following format when reasoning:

Question: the input question
Thought: reasoning about what to do
Action: the action to take (one of [{tool_names}])
Action Input: the input to the action
Observation: the result of the action 
... (repeat if needed)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
{agent_scratchpad}
"""

tools = [get_system_time]

prompt = PromptTemplate.from_template(custom_prompt)

agent = create_react_agent(model, tools, prompt)

agent_executer = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = "Get the current time in Toronto only (no date)"

result = agent_executer.invoke({"input": query})

print("Agent final output:", result)

# -------------------------
# QUICK SUMMARY (plain words)
# -------------------------
# - ChatOpenAI: talks to the OpenAI model.
# - @tool: makes a function callable by the agent (exposes name + description).
# - get_system_time: a simple tool that returns system time (use timezone-aware code to ensure IST).
# - PromptTemplate/custom_prompt: tells the model how to format thinking steps and where to put tool results.
# - {agent_scratchpad}: required for ReAct — this is the working memory for the agent's intermediate steps.
# - create_react_agent: constructs an agent that can think and call tools in a loop (ReAct pattern).
# - AgentExecutor: runs that agent loop and returns the final answer; verbose=True shows the internal steps.