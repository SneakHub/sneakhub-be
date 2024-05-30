from datetime import datetime
from typing import ClassVar

import pytz
from pydantic import BaseModel, Field
from uuid import uuid4

def get_current_datetime_with_tz():
    tz = pytz.timezone('Asia/Ho_Chi_Minh')
    return datetime.now(tz=tz)

# Util classes for schemas
class UUID4Factory(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

class createdAndUpdatedAtTimeInitializationFactory(BaseModel):
    # Set the timezone to Vietnam (UTC+7)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # pydantic.errors.PydanticUserError: A non-annotated attr
    # ibute was detected: `tz = <DstTzInfo 'Asia/Ho_Chi_Minh' LMT+7:07:00 STD>`. A
    # ll model fields require a type annotation; if `tz` is not meant to be a fiel
    # d, you may be able to resolve this error by annotating it as a `ClassVar` or updating `model_config['ignored_types']`.
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # tz: ClassVar[pytz.timezone] = pytz.timezone('Asia/Ho_Chi_Minh')
    # current_datetime: ClassVar[datetime] = datetime.now(tz=tz)

    created_at: datetime = Field(default_factory= lambda: get_current_datetime_with_tz())
    updated_at: datetime = Field(default_factory=lambda: get_current_datetime_with_tz())


