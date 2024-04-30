from ...schemas.item import BaseItem, Item
from typing import List, Union
from ...utils.list import find

# create a clone database of Item List
items: List[Item] = []

def find_all() -> list[Item]:
    global items
    return items
