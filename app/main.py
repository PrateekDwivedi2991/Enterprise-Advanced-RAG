from fastapi import FastAPI
from app.api import admin,auth

app = FastAPI(title="Enterprise RAG",version="0.1.0-lession-0")

app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

