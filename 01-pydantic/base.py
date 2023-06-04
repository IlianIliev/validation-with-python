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


def no_data():
    try:
        User()
    except pydantic.ValidationError as e:
        print("Without any input, validation error is thrown:\n", e.json())


# I. Without any input, validation error is thrown:
# no_data()

# II. Different way to create a user and validate it
regular_user = User(id=1, name="John Doe", email="john_doe@example.org")
json_user = User.parse_raw(
    '{"id": 1, "name": "John Doe", "email": "john_doe@example.org"}'
)
dict_user = User.parse_obj(
    {"id": 1, "name": "John Doe", "email": "john_doe@example.org"}
)

assert regular_user == json_user == dict_user


# III. Example of data conversion
john = User(id=1, email="john_doe@example.org", date_of_birth="1990-01-01")
# print("{} - {}".format(john.date_of_birth, type(john.date_of_birth)))


# IV. Providing invalid format results in a validation error
# User(id=1, email="john_doe@example.org", date_of_birth="1990-21-01")


# V. Custom validation error
def with_age():
    try:
        User(id=1, email="john_doe@example", age=17)
    except pydantic.ValidationError as e:
        print("Under-aged user validation error:\n", e.json())


# with_age()
