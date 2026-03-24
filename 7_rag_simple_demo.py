from langchain_community.document_loaders.parsers import PyPDFParser
from langchain_core.documents.base import Blob
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = OpenAIEmbeddings(model="text-embedding-3-small")

blob = Blob.from_path(r"D:\Resume\resume_da.pdf")
parser = PyPDFParser()
documents = parser.lazy_parse(blob)
docs = [doc for doc in documents]

spliter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)
chunks = spliter.split_documents(docs)
print(f"Number of chunks created: {len(chunks)}")

vector_store = FAISS.from_documents(documents=chunks,embedding=model)
vector_store.save_local("faiss_index")
retriever = vector_store.as_retriever(search_kwargs={"k": 2})
query = "What is the experience of Krishna Kant Sahu in AI?"
docs = retriever.invoke(query)

print("Retrieved documents:")
for doc in docs:
    print(doc.page_content)
    print("--------------------------------")

prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful assistant that answers the details based on the context provided.
    Context: {context}
    Question: {question}
    """
)

# 🔟 Initialize the Chat Model (LLM)
llm = ChatOpenAI(model="gpt-5-nano")

# 11️⃣ Combine prompt + model into a chain
chain = prompt | llm

# 12️⃣ Run the chain with context and question
user_input = {"context": docs, "question": query}
response = chain.invoke(user_input)

print("Response:")
print(response.content)