from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from typing import List
import os

#here we are dealing with loading the document(pdf/txt)
def load_document(file_path: str) -> List:
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
        docs = loader.load()

    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        docs = [Document(page_content=text, metadata={"source": file_path})]

    else:
        raise ValueError("Unsupported file type")

    for doc in docs:
        doc.metadata["source"] = file_path
        doc.metadata["file_type"] = ext

    return docs
