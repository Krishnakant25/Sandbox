from dotenv import load_dotenv
from langchain_community.document_loaders.parsers import PyPDFParser
from langchain_core.documents.base import Blob
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

load_dotenv()

model = OpenAIEmbeddings(model="text-embedding-3-small")

blob = Blob.from_path(r"D:\Resume\resume_da.pdf")
parser = PyPDFParser()
documents = parser.lazy_parse(blob)
docs = [doc for doc in documents]

spliter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)
chunks = spliter.split_documents(docs)
print(f"Number of chunks created: {len(chunks)}")

vector_store = FAISS.from_documents(documents=chunks, embedding=model)

vector_store.save_local("faiss_index")

query = "AI engineer"
results = vector_store.similarity_search(query, k=3)

print(f"Results for query '{query}':")
for i, result in enumerate(results):
    print(f"Result {i+1}:")
    print(f"Content: {result.page_content}")
    print(f"Metadata: {result.metadata}")
    print("--------------------------------")

# 8️⃣ You can also reload FAISS later
new_store = FAISS.load_local("faiss_index", embeddings=model, allow_dangerous_deserialization=True)