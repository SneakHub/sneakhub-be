# from fastapi import FastAPI
#
# app = FastAPI()
# @app.get("/")
# async def read_root():
#     return {"message": "Hello World!"}

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}