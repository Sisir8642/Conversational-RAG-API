from services.embedding import EmbeddingService
from services.vector_store import VectorStore
from services.llm import LLMService
from services.rag import RAGService

# here we have Initialize services ONCE so it could be access easily

embedder = EmbeddingService()
vector_store = VectorStore()
llm_service = LLMService()

rag_service = RAGService(
    vector_store=vector_store,
    embedder=embedder,
    llm=llm_service
)
