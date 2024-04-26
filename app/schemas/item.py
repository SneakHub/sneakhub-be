from pydantic import BaseModel
from ..utils.factory import UUID4Factory

# classes of Item schema


class BaseItem(BaseModel):
    name: str
    quantity: int


class Item(UUID4Factory, BaseItem):
    pass
