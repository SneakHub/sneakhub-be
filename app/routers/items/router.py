# This file is to declare the routes for the CRUD operations

from typing import List
from fastapi import APIRouter

from . import services
from .dto import CreateItemRequest, UpdateItemRequest
from ...schemas import Item

# A router to handle the CRUD operations for items
router = APIRouter()


@router.get("", response_model=List[Item])
async def find_all():
    return services.find_all()


@router.get("/{item_id}", response_model=Item)
async def find_one(item_id: str):
    return services.find_one(item_id)


@router.post("", response_model=Item)
async def create_one(request: CreateItemRequest):
    return services.create_one(request)


@router.put("/{item_id}", response_model=Item)
async def update_one(item_id: str, request: UpdateItemRequest):
    return services.update_one(item_id, request)


@router.delete("/{item_id}", response_model=Item)
async def delete_one(item_id: str):
    return services.delete_one(item_id)
