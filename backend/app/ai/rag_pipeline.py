from typing import List, Dict, Any
import uuid
from app.ai.vector_store import vector_store

def load_resource_chunks(text: str, chunk_size: int = 500) -> List[str]:
    """Split extracted text into manageable chunks."""
    # TODO: Implement LangChain RecursiveCharacterTextSplitter
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def retrieve_relevant_chunks(query: str, resource_id: uuid.UUID) -> List[str]:
    """Retrieve relevant chunks from vector store."""
    return vector_store.similarity_search(query, resource_id)

def build_context(query: str, resource_id: uuid.UUID) -> Dict[str, Any]:
    """Build structured context from retrieved chunks."""
    chunks = retrieve_relevant_chunks(query, resource_id)
    return {
        "query": query,
        "context": "\n".join(chunks),
        "chunk_count": len(chunks)
    }
