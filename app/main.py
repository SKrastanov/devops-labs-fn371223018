import os
import asyncpg
from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

class Note(BaseModel):
    title: str
    body: str

async def get_repository():
    # Database dependency provider expected by tests
    DATABASE_URL = os.environ.get("DATABASE_URL", os.environ.get("TEST_DATABASE_URL"))
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/notes")
async def create_note(note: Note, conn = Depends(get_repository)):
    await conn.execute("INSERT INTO notes (title, body) VALUES ($1, $2)", note.title, note.body)
    return {"status": "success"}
