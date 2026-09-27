# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title="NoteVault AI API",
    debug=True
)

# TODO: Add CORS middleware

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Welcome to NoteVault AI API"}
