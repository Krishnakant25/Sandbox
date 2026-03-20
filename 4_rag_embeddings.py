from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

model = OpenAIEmbeddings(model="text-embedding-3-small")

text = ["The quick brown fox jumps over the lazy dog.",
        "Artificial intelligence is the simulation of human intelligence in machines.",
        "LangChain is a framework for building applications with LLMs.",
        "Embeddings are numerical representations of text that capture semantic meaning."]

embedings = model.embed_documents(text)

print(embedings)

for i, em in embedings:
    print(f"Total dimension in each embedding vector: {len(em)} Text {i+1}: {em[:10]}...")