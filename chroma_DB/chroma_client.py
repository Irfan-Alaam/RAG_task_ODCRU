import chromadb
from chromadb.config import Settings
import os

def get_chroma_client():
    persist_dir = os.path.join(os.path.dirname(__file__), "db")
    os.makedirs(persist_dir, exist_ok=True)
    
    return chromadb.PersistentClient(
        path=persist_dir,
        settings=Settings(
            anonymized_telemetry=False,
            allow_reset=True
        )
    )