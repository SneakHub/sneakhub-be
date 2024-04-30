from pydantic import BaseModel, Field
from uuid import uuid4


# Util classes for schemas
class UUID4Factory(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
