from pydantic import BaseModel
from typing import Union

class BaseItem(BaseModel):
    name: str
    quantity: str

class Item(baseItem):
    pass