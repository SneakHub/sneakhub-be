# This file is to simulate the database operations

from typing import List, Union

from ...schemas.item import BaseItem, Item
from ...utils.list import find

# Simulate as a item database
items: List[Item] = []


def find_all() -> List[Item]:
    return items


def find_one(id: str) -> Item:
    item = find(lambda item: item.id == id, items)
    if not item:
        raise Exception(f"Item with id {id} not found")
    return item


def create_one(data: BaseItem) -> Item:
    global items
    item = Item(**data.dict())
    # Add the created item to the database
    items = [*items, item]
    return item


def delete_one(id: str) -> Union[None, Item]:
    global items
    item = find(lambda item: item.id == id, items)
    if not item:
        return None
    # Delete the existing item from the database
    items = list(filter(lambda item: item.id != id, items))
    return item


def update_one(id: str, data: Item) -> Item:
    global items
    item = find(lambda item: item.id == id, items)
    if not item:
        raise Exception(f"Item with id {id} not found")
    # Update the existing item
    items = list(map(lambda item: data if item.id == id else item, items))
    return data
