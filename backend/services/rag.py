class RAGService:
    def __init__(self, vector_store, embedder, llm):
        self.vector_store = vector_store
        self.embedder = embedder
        self.llm = llm

    def query(self, question: str):
        query_emb = self.embedder.embed([question])[0]
        results = self.vector_store.search(query_emb)
        if not results:
            return "No relevant information found in the document."


        context = "\n\n".join([
        r.payload["content"][:500] for r in results
    ])

        return self.llm.generate(question, context)
