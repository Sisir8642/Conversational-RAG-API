from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np
 
 #initialize the model and txt
class EmbeddingService:
    def __init__(self, model_name: str ="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        
    def embed(self, text: List[str]) -> np.ndarray:
        return self.model.encode(text)