from ...schemas.item import BaseItem, Item
from typing import List, Union
from ...utils.list import find

# create a clone database of Item List
items: List[Item] = []

def find_all() -> list[Item]:
    return items

def find_one(id: str) -> Union[Item, None]:
    item = find(lambda item: item.id == id, items)
    if not item:
        raise Exception(f"no item with value={id} is found!")
    return item
