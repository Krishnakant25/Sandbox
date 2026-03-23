from langchain_community.document_loaders.parsers import PyPDFParser
from langchain_core.document_loaders.blob_loaders import Blob
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

model = OpenAIEmbeddings(model="text-embedding-3-small")

blob = Blob.from_path(r"D:\Resume\resume_da.pdf")

parser = PyPDFParser()

documents = parser.lazy_parse(blob)

docs = []
for doc in documents:
    docs.append(doc)
print(docs)

spliter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 50
)


chunks = spliter.split_documents(docs)
print(f"Number of chunks created: {len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:")
    print(chunk.page_content)  # Print the content of each chunk
    print("--------------------------------")

embeddings = model.embed_documents([c.page_content for c in chunks])

print("Embeddings:")
for (i, emb), c in zip (enumerate(embeddings),chunks):
    print(f"For the text: {c.page_content}")
    print(f"Total Dimensions: {len(emb)} Chunk {i+1} Embedding: {emb[:10]}...")  # Print first 10 dimensions of the embedding for brevity
    print("--------------------------------") 