from typing import List
from app.core.config import get_settings

settings = get_settings()

def create_embeddings(text: str) -> List[float]:
    """Generate vector embedding for a single text chunk."""
    # TODO: Implement OpenAI Embeddings interface
    return [0.0] * 1536  # Mock embedding

def batch_embeddings(texts: List[str]) -> List[List[float]]:
    """Generate vector embeddings for multiple text chunks."""
    # TODO: Implement batched OpenAI Embeddings interface
    return [[0.0] * 1536 for _ in texts]
