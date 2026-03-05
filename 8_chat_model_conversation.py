from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

chat_history = []

sys_msg = SystemMessage(content="You are a helpfull AI assistant")
chat_history.append(sys_msg)

while True:
    query = input("You:")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print(f"AI response: {response}")

print(chat_history)
