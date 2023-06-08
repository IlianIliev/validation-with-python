from typing import Optional

import pydantic
from pydantic import BaseModel, EmailStr, validator
from datetime import date


class UnderAgedValueError(pydantic.PydanticValueError):
    code = "under-aged"
    msg_template = "Under-aged users are not allowed."


class User(BaseModel):
    id: int
    name: Optional[str]
    email: EmailStr
    date_of_birth: Optional[date]
    age: Optional[int]

    @validator("age")
    def validate_age(cls, age):
        if age < 18:
            raise UnderAgedValueError()
        return age
