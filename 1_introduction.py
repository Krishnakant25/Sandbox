from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano",temperature=0.3,max_completion_tokens=1000)

response = model.invoke("what is the capital of China?")

print(response.content)