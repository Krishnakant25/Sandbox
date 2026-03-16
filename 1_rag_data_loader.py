from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI

loader = TextLoader("agentic-ai-sample.txt", encoding="utf-8")

documents = loader.load()

print(f"Number of documents loaded: {len(documents)}")

print(documents)