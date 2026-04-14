# ------------------------
# Imports and environment
# ------------------------
from typing import Annotated
from typing_extensions import TypedDict
from langchain.chat_models import init_chat_model     # helper to init chat LLMs
from langchain_tavily import TavilySearch             # Tavily search tool wrapper for LangChain
from langgraph.graph import StateGraph, START, END    # LangGraph core classes
from langgraph.graph.message import add_messages      # helper to append messages to state
from langgraph.prebuilt import ToolNode, tools_condition

# ToolNode → Runs the tool when the LLM requests a tool call.
# tools_condition → Checks whether the LLM wants a tool and routes the graph accordingly.

from dotenv import load_dotenv

# Load environment variables from .env into os.environ. This reads API keys.
load_dotenv()

# ------------------------
# 1. Define the shape of state
# ------------------------
class State(TypedDict):
    """
    TypedDict schema for the state that flows through the graph.

    - messages: a list of chat messages (each message is typically a dict like
                {"role": "user"/"assistant"/"system", "content": "..."}).
      We annotate it with add_messages so that LangGraph knows to append messages
      to the existing list instead of replacing it when nodes return new messages.
    """
    messages: Annotated[list, add_messages]


# ------------------------
# 2. Create a graph builder
# ------------------------
# StateGraph(State) creates a builder that accepts/validates states with the shape defined above.
graph_builder = StateGraph(State)


# ------------------------
# 3. Initialize model and tools
# ------------------------
# init_chat_model is a convenience wrapper that returns a chat model instance.
# Here we specify "openai:gpt-5-nano" (the provider prefix indicates OpenAI).
# The returned model object exposes methods like `invoke()` and `bind_tools()`.
model = init_chat_model("openai:gpt-5-nano")

# TavilySearch is the LangChain wrapper that allows the LLM to perform web searches.
# max_results=2 instructs the tool to return up to 2 search results per call.
tool = TavilySearch(max_results=2)

# If you have multiple tools, put them in this list.
tools = [tool]

# bind_tools attaches the tool wrappers to the model so the model can choose to call them.
# The returned object (llm_with_tools) behaves like a chat model but will route tool calls
# when the model produces tool-invocation actions.
llm_with_tools = model.bind_tools(tools)


# ------------------------
# 4. Define the chatbot node function
# ------------------------
def chatbot(state: State) -> dict:
    """
    Chatbot node function for the graph.

    Inputs:
      - state: the current State dictionary (must conform to State TypedDict).
               e.g. {"messages": [{"role": "user", "content": "Hello"}]}

    Behavior:
      - Calls the LLM (with tools bound) to generate a response using existing messages.
      - Returns a dictionary representing updates to the state. Here we return
        {"messages": [<assistant_message>]} so that add_messages will append
        the assistant's message to the state's messages list.

    Returns:
      - A dict mapping keys in State to values to update. LangGraph will merge this into
        the running state according to the schema and annotations (e.g., add_messages).
    """
    # llm_with_tools.invoke expects a list of messages (the chat history).
    # It returns an assistant message object (often a LangChain message wrapper) which
    # contains .content and .role depending on the model wrapper implementation.
    assistant_message = llm_with_tools.invoke(state["messages"])
    # We return a dictionary with "messages": [assistant_message] — add_messages will append it.
    return {"messages": [assistant_message]}


# ------------------------
# 5. Add chatbot node to the builder
# ------------------------
# This registers a node named "chatbot" that will run the chatbot(state) function.
graph_builder.add_node("chatbot", chatbot)


# ------------------------
# 6. Create and add ToolNode
# ------------------------
# ToolNode is a prebuilt node that knows how to call one or more tool wrappers
# (like TavilySearch), format their inputs/outputs, and inject results back into the state.
tool_node = ToolNode(tools=tools)

# Add the tool node to the graph builder under the name "tools".
graph_builder.add_node("tools", tool_node)


# ------------------------
# 7. Connect nodes with edges and conditional edges
# ------------------------
# Add conditional edges from "chatbot" node using tools_condition.
# tools_condition is a helper that inspects the LLM output and decides if a tool
# should be called. If tools are needed, the flow will route to the "tools" node.
graph_builder.add_conditional_edges("chatbot", tools_condition)

# After "tools" are run, route back to "chatbot" so the model can integrate tool outputs.
graph_builder.add_edge("tools", "chatbot")

# Start the graph at chatbot when the workflow begins.
graph_builder.add_edge(START, "chatbot")

# Optional: explicitly add chatbot -> END if you want explicit termination path.
# Here we let the graph's compiled flow and conditions determine termination.
graph_builder.add_edge("chatbot", END)


# ------------------------
# 8. Compile graph
# ------------------------
# compile() validates node connectivity, checks start/end, prepares runtime structures,
# and returns a runnable Graph instance with methods like .invoke(), .stream(), .get_graph()
graph = graph_builder.compile()


# ------------------------
# 9. Save graph visualization
# ------------------------
# draw_mermaid_png returns PNG bytes of a Mermaid-rendered diagram.
png_data = graph.get_graph().draw_mermaid_png()
with open("2_simple_chatbot.png", "wb") as f:
    f.write(png_data)

print("Graph saved as 2_simple_chatbot.png")


# ------------------------
# 10. Streaming helper function
# ------------------------
def stream_graph_updates(user_input: str):
    """
    Stream updates from the compiled graph for a single user input.

    How it works:
      - Wraps the user message as a list of messages and pushes it into http://graph.stream()
      - http://graph.stream() yields events as nodes produce partial or full state updates (depending on implementation)
      - We iterate events and print the latest assistant response from each yielded value.

    Parameters:
      - user_input: a string typed by the user

    Notes:
      - Each event returned by http://graph.stream() is typically a mapping where the values
        are partial state dicts. We access the last message with value["messages"][-1].
      - Use this function when you want to stream intermediate outputs while the LLM/tool
        run completes (e.g., streaming tokens or multiple node outputs).
    """
    # Prepare the initial state with the user's message; add_messages will ensure it's appended to history
    initial_state = {"messages": [{"role": "user", "content": user_input}]}

    # http://graph.stream returns an iterator; it yields events while nodes run (useful for streaming).
    for event in graph.stream(initial_state):
      
        # Each event contains:

        # What a node just produced

        # Example:

        # Chatbot reply

        # Tool output

        # Final answer

        # We loop through them one by one.
        # Each event may contain multiple values (states for different branches/nodes).
        for value in event.values():
            # value is a state-like dict. We print the last assistant message's content.
            # The exact structure of the assistant message (e.g., .content attribute) can vary
            # depending on the model wrapper; here we assume the returned object has .content.
            assistant_msg = value["messages"][-1]
            # This means:

            # Look at all messages so far

            # Take the last one

            # That last one is usually the assistant’s reply
            # Some wrappers return a plain dict, others return a Message object. Handle both.
            if hasattr(assistant_msg, "content"):
                print("Assistant:", assistant_msg.content)
            elif isinstance(assistant_msg, dict) and "content" in assistant_msg:
                print("Assistant:", assistant_msg["content"])
            else:
                # Fallback: print the representation of the message object
                print("Assistant:", repr(assistant_msg))


# ------------------------
# 11. Main interactive loop
# ------------------------
def main_loop():
    """
    A simple REPL (read-eval-print loop) for the chatbot.

    - Takes user input from stdin
    - Streams responses via stream_graph_updates()
    - Terminates when the user types 'quit', 'exit', or 'q'
    """
    print("Chatbot is ready! Type 'quit', 'exit', or 'q' to stop. \n")

    while True:
        try:
            # Ask for user input
            user_input = input("User: ")

            # Allow exit commands
            if user_input.strip().lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            # Stream responses for this user input
            stream_graph_updates(user_input)

        except KeyboardInterrupt:
            # Allow graceful exit on Ctrl+C
            print("\nInterrupted. Goodbye!")
            break
        except Exception as e:
            # Print error and break the loop. Helpful for debugging runtime issues like missing keys.
            print("Error:", e)
            break


# If this file is executed as a script, start the main loop
if __name__ == "__main__":
    main_loop()