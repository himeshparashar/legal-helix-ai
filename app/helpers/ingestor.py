import os
from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = PyPDFLoader("data.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

texts = text_splitter.split_documents(documents)

# Load the embedding model
model_name = "BAAI/bge-large-en"
model_kwargs = {'device':'cpu'}
encode_kwargs = {'normalize_embeddings': False}

embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

print("Embedding Model Loaded")
collection_name = "legal_helix_ai"

qdrant = Qdrant.from_documents(
    texts,
    embeddings,
    url=os.environ.get("QDRANT_URL"),
    api_key=os.environ.get("QDRANT_KEY"),
    prefer_grpc = False,
    collection_name = collection_name
)

print("Qdrant Collection Created")