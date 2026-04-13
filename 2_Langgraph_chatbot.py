from typing import Annotated, TypedDict
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

load_dotenv()

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

model = ChatOpenAI(model="gpt-5-nano", temperature=1.1)

def chatbot(state: State):
    """
    Receives the current conversation state,
    calls the OpenAI model,
    and appends the assistant response.
    """
    response = model.invoke(state["messages"])
    return {"messages": [response]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

mermaid_code = graph.get_graph().draw_mermaid()

with open("1_simple_chatbot.mmd", "w", encoding="utf-8") as f:
    f.write(mermaid_code)

print("✅ Mermaid graph saved as 1_simple_chatbot.mmd")
print("➡️ Open https://mermaid.live to export PNG if needed")

def stream_graph_updates(user_input: str):
    """
    Streams responses from the chatbot node
    as soon as they are produced.
    """
    for event in graph.stream(
        {"messages": [{"role": "user", "content": user_input}]}
    ):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

if __name__ == "__main__":
    print("🤖 Chatbot is ready! Type 'quit', 'exit', or 'q' to stop.\n")

    while True:
        try:
            user_input = input("User: ")

            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            stream_graph_updates(user_input)

        except Exception as e:
            print("Error:", e)
            break