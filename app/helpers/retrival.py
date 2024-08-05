import os
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import models, QdrantClient






async def retrieverfn():

    model_name = "BAAI/bge-large-en"
    model_kwargs = {'device':'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
    )
    doc_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="legal_helix_ai",
    url=os.environ.get("QDRANT_URL"),
    api_key=os.environ.get("QDRANT_KEY"),
    )

    retriever = doc_store.as_retriever()
    return retriever
