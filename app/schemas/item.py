from pydantic import BaseModel
from typing import Union
from app.utils.factory import UUID4Factory


class BaseItem(BaseModel):
    name: str
    quantity: str

class Item(BaseItem, UUID4Factory):
    pass