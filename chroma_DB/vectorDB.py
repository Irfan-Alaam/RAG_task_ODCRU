from chroma_DB.chroma_client import get_chroma_client
from chroma_DB.semantic import encode_chunks
from src.loader import load_data
from src.chunk import chunk
from src.config import DATA_PATH

def clean_metadata(meta: dict) -> dict:
    clean = {}
    for k, v in meta.items():
        if v is None:
            continue
        if isinstance(v, (str, int, float, bool)):
            clean[k] = v
        else:
            clean[k] = str(v)
    return clean


def build_vector_store(model):
    client = get_chroma_client()
    collection = client.get_or_create_collection(
        name="linuxDB",
        metadata={"hnsw:space": "cosine"}
    )

    if collection.count() > 0:
        print("->->->->Vector DB already populated — skipping embedding")
        return collection
    
    print("!!!Creating embeddings and populating ChromaDB...")

    data = load_data(DATA_PATH)
    chunks = chunk(data)
    # print(f"Created {len(chunks)}")
    # print(chunks[3])
    ids, documents, metadatas = [], [], []

    for i, c in enumerate(chunks):
        ids.append(f"chunk_{i}")
        documents.append(c["text"])
        metadatas.append(clean_metadata(c["metadata"]))

    embeddings = encode_chunks(chunks, model)

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings.tolist()
    )
    
    print(f"--> Stored {len(ids)} vectors in ChromaDB <--")
    return collection

