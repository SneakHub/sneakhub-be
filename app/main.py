from fastapi import FastAPI
from typing import Union

from app.config import get_settings

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/test/read_env")
async def read_env():
    settings = get_settings()
    return settings