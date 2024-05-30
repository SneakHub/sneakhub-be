# This file is to declare the routes for the CRUD operations

from typing import List
from fastapi import APIRouter

from . import services
from .dto import CreateToDoRequest, UpdateToDoRequest
from ...schemas.todo import BaseTodo, ToDo

# A router to handle the CRUD operations for todos
router = APIRouter()


@router.get("", response_model=List[ToDo])
async def find_all():
    return services.find_all()


@router.get("/{todo_id}", response_model=ToDo)
async def find_one(todo_id: str):
    return services.find_one(todo_id)


@router.post("", response_model=ToDo)
async def create_one(request: CreateToDoRequest):
    return services.create_one(request)


@router.put("/{todo_id}", response_model=ToDo)
async def update_one(todo_id: str, request: UpdateToDoRequest):
    return services.update_one(todo_id, request)


@router.delete("/{todo_id}", response_model=ToDo)
async def delete_one(todo_id: str):
    return services.delete_one(todo_id)
