from datetime import datetime

from pydantic import BaseModel

from app.utils.factory import UUID4Factory


class BaseToDos(BaseModel):
    title: str
    created_at: datetime
    updated_at: datetime
    done: bool


class ToDos(UUID4Factory, BaseToDos):
    pass

