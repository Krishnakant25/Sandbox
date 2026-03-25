from langchain_community.document_loaders.parsers import PyPDFParser
from langchain_core.documents.base import Blob
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain
from langchain_community.vectorstores import FAISS

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
llm = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

blob = Blob.from_path(r"D:\Resume\resume_da.pdf")
parser = PyPDFParser()
documents = parser.lazy_parse(blob)
docs = [doc for doc in documents]

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)

chunks = splitter.split_documents(docs)

vector_store = FAISS.from_documents(documents=chunks, embedding=embeddings)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

query = "What is the experience in generative AI?"
docs = retriever.invoke(query)

# print docs
print("Retrieved Context is as follows: ")
print(docs)
print("---------------")
for i, d in enumerate(docs):
    print(f"{i+1} context is:")
    print(d.page_content)
    print("***************")

prompt = ChatPromptTemplate.from_template(
    """"Answer the question based only on the provided context.
    context: {context}
    question: {question}"""
)

llm_chain = prompt | llm

user_input = {"context": docs, "question": query}
result = llm_chain.invoke(user_input)
print("Output from RAG:")
print(result.content)


@chain
def rag_pipeline(query):
    docs = retriever.invoke(query)
    llm_chain = prompt | llm
    user_input = {"context": docs, "question": query}
    result = llm_chain.invoke(user_input)
    return result.content

result = rag_pipeline.invoke(query)
print("Output from RAG:")
print(result)