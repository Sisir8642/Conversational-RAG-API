from fastapi import APIRouter, UploadFile, File
import os
from services.dependencies import embedder, vector_store
from services.loader import load_document
from services.chunking import chunk_fixed, chunk_overlap


router = APIRouter()
#here we access the /upload where we would upload .pdf and .txt files
@router.post("/upload")
async def upload(file: UploadFile = File(...), strategy: str = "fixed"):
    
    if not (file.filename.endswith(".pdf") or file.filename.endswith(".txt")):
        return {"error": "Only PDF and TXT files are supported"}
    
    path = f"temp_{file.filename}"
    
    with open(path, "wb") as f:
        f.write(await file.read())

    docs = load_document(path)

    if strategy == "fixed":
        chunks = chunk_fixed(docs)
    else:
        chunks = chunk_overlap(docs)

    texts = [doc.page_content for doc in chunks]
    embeddings = embedder.embed(texts)

    vector_store.add(chunks, embeddings)

    return {"message": "Processed successfully"}
