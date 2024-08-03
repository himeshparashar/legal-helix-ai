import os
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_qdrant import QdrantVectorStore



model_name = "BAAI/bge-small-en"
model_kwargs = {"device": "cpu"}
encode_kwargs = {"normalize_embeddings": True}
embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
)

async def similarity_search(query: str):
    doc_store = QdrantVectorStore.from_existing_collection(
    embeddings=embeddings,
    collection_name="legal_helix_ai",
    url=os.environ.get("QDRANT_URL"),
    api_key=os.environ.get("QDRANT_KEY"),
    )
