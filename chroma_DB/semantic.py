from typing import List, Dict
from sentence_transformers import SentenceTransformer

def encode_chunks(chunks: List[Dict], model: SentenceTransformer):
    texts = [c["text"] for c in chunks]
    return model.encode(
        texts,
        batch_size=16,
        convert_to_numpy=True,
        normalize_embeddings=True
    )
