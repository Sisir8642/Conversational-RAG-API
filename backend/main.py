from fastapi import FastAPI
from routes import upload, chat

app = FastAPI(title="RAG Backend API")

app.include_router(upload.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
