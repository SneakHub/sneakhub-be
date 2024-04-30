from pydantic import BaseModel, Field
from uuid import uuid4

class UUID4Factory(BaseModel):
    id: str = Field(default_factory= lambda: str(uuid4()))