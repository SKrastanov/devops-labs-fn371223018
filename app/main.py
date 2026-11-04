import os

import asyncpg
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Note(BaseModel):
    title: str
    body: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/notes")
async def create_note(note: Note):
    conn = await asyncpg.connect(os.environ["DATABASE_URL"])
    await conn.execute(
        "INSERT INTO notes (title, body) VALUES ($1, $2)", note.title, note.body
    )
    await conn.close()
    return {"status": "success"}
