# This file is to declare the routes for the CRUD operations

from typing import List
from fastapi import APIRouter

from . import services
from .dto import CreateToDosRequest, UpdateToDosRequest
from ...schemas.todos import BaseToDos, ToDos

# A router to handle the CRUD operations for todos
router = APIRouter()


@router.get("", response_model=List[ToDos])
async def find_all():
    return services.find_all()


@router.get("/{todo_id}", response_model=ToDos)
async def find_one(todo_id: str):
    return services.find_one(todo_id)


@router.post("", response_model=ToDos)
async def create_one(request: CreateToDosRequest):
    return services.create_one(request)


@router.put("/{todo_id}", response_model=ToDos)
async def update_one(todo_id: str, request: UpdateToDosRequest):
    return services.update_one(todo_id, request)


@router.delete("/{todo_id}", response_model=ToDos)
async def delete_one(todo_id: str):
    return services.delete_one(todo_id)
