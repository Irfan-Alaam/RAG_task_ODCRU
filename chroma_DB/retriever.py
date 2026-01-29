from src.config import TOP_K
class ChromaRetriever:
    def __init__(self, collection, model, top_k=TOP_K):
        self.collection = collection
        self.model = model
        self.top_k = top_k

    def query(self, query_text: str):
        query_emb = self.model.encode([query_text], convert_to_numpy=True, normalize_embeddings=True)

        results = self.collection.query(
            query_embeddings=query_emb.tolist(),
            n_results=self.top_k,
            include=['documents', 'metadatas', 'distances']
        )

        if not results['documents'][0]:
            return []

        output = []
        for doc, meta, score in zip(results['documents'][0], results['metadatas'][0], results['distances'][0]):
            output.append({
                "text": doc,
                "score": score,
                "type": meta.get("type", "unknown"),
                "name": meta.get("name", meta.get("title", "Unknown"))
            })
        return output
