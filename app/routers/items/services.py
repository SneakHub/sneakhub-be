from ...schemas.item import BaseItem, Item
from typing import List, Union
from ...utils.list import find

# create a clone database of Item List
items: List[Item] = []

def find_all() -> List[Item]:
    return items

def find_one(id: str) -> Union[Item, None]:
    item = find(lambda item: item.id == id, items)
    if not item:
        raise Exception(f"no item with value={id} is found!")
    return item

def create_one(data: BaseItem) -> Item:
    global items
    item = Item(**data.dict())

    # add new item into the database
    items = [*items, item]
    return item

def delete_one(id: str) -> Union[Item, None]:
    global items
    item = find(lambda item: item.id == id, items)
    if not item:
        return None
    # delete the found item
    items = list(filter(lambda item: item.id != id, items))
    return item


def update_one(id: str, data: Item) -> Item:
    global items
    item = find(lambda item: item.id == id, items)
    if not item:
        raise Exception(f"no item with value={id} is found!")

    # delete the found item
    items = list(map(lambda item: data if item.id == id else item, items))
    return item


