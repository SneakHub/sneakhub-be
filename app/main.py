from ctypes import Union

from fastapi import FastAPI

from .routers.items.router import router as items_router
from .routers.todos.router import router as todos_router

from .constants import Tags

from app.config import get_settings

app = FastAPI()

app.include_router(items_router, prefix=f"/{Tags.ITEMS.value}", tags=[Tags.ITEMS])
app.include_router(todos_router, prefix=f"/{Tags.TODOS.value}", tags=[Tags.TODOS])

@app.get("/")
async def root():
    return {"message": "Hello World!"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# test configuration between decoded credentials stored in local environment and program
# @app.get("/test/read_env")
# async def read_env():
#     settings = get_settings()
#     return settings
