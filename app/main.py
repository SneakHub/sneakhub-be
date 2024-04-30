from fastapi import FastAPI

from .routers.items.router import router as items_router
from .constants import Tags

app = FastAPI()

app.include_router(items_router, prefix=f"/{Tags.ITEMS.value}", tags=[Tags.ITEMS])


@app.get("/")
async def root():
    return {"message": "Hello World!"}
