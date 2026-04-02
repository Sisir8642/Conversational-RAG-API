from langchain_community.document_loaders import PyPDFLoader
from typing import List

def load_document(file_path: str) -> List:
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    
    for doc in docs:
        doc.metadata["source"] = file_path
        
    return docs