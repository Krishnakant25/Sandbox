from langchain_community.document_loaders.parsers.pdf import PyPDFParser
from langchain_core.documents.base import Blob

blob = Blob.from_path("./Krishna_kant_resume.pdf")

parser = PyPDFParser()

document = parser.lazy_parse(blob)

docs = []

for doc in document:
    docs.appened(doc)

print(doc)