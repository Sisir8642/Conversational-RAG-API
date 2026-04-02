from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import uuid

#here we have used qdrant for vector storage
class VectorStore:
    def __init__(self):
        self.client = QdrantClient(":memory:")
        self.collection = "docs"

        self.client.recreate_collection(
            collection_name=self.collection,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )

    def add(self, documents, embeddings):
        points = [
            PointStruct(
                id=str(uuid.uuid4()),
                vector=emb.tolist(),
                payload={"content": doc.page_content, "metadata": doc.metadata}
            )
            for doc, emb in zip(documents, embeddings)
        ]
        self.client.upsert(collection_name=self.collection, points=points)

    def search(self, query_embedding, top_k=5):
        results = self.client.query_points(
            collection_name=self.collection,
            query=query_embedding.tolist(),
            limit=top_k
        )

        return results.points
