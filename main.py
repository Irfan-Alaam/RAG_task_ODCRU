from dotenv import load_dotenv
load_dotenv()
import os
import uvicorn
from src.config import MODEL_PATH, EMBEDDING_MODEL, DEVICE
from chroma_DB.vectorDB import build_vector_store
from chroma_DB.retriever import ChromaRetriever
from llm.groq import load_groq_llm
from rag.prompt import RAG_PROMPT
from rag.rag_chain import RAGChain
from sentence_transformers import SentenceTransformer
from UI import api
print("---> Linux Knowledge RAG System <---")

if os.path.exists(MODEL_PATH):
    model = SentenceTransformer(MODEL_PATH, device=DEVICE)
else:
    model = SentenceTransformer(EMBEDDING_MODEL, device=DEVICE)
    os.makedirs(MODEL_PATH, exist_ok=True)
    model.save(MODEL_PATH)

collection = build_vector_store(model)

retriever = ChromaRetriever(collection, model)
llm = load_groq_llm()

rag = RAGChain(
    retriever=retriever,
    llm=llm,
    prompt=RAG_PROMPT
)
api.set_rag(rag)

if __name__ == "__main__":
    uvicorn.run("UI.api:app", host="127.0.0.1", port=8000, reload=True)
