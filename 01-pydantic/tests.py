from datetime import date

import pytest
import pydantic

from base import User
from extended import BusinessUser


def test_without_any_input_it_raises_validation_error():
    with pytest.raises(pydantic.ValidationError) as e:
        User()

    assert e.value.errors() == [
        {"loc": ("id",), "msg": "field required", "type": "value_error.missing"},
        {"loc": ("email",), "msg": "field required", "type": "value_error.missing"},
    ]


def test_different_ways_to_create_a_user():
    regular_user = User(id=1, name="John Doe", email="john_doe@example.org")
    json_user = User.parse_raw(
        '{"id": 1, "name": "John Doe", "email": "john_doe@example.org"}'
    )
    dict_user = User.parse_obj(
        {"id": 1, "name": "John Doe", "email": "john_doe@example.org"}
    )

    assert regular_user == json_user == dict_user


def test_data_conversion():
    # III. Example of data conversion
    john = User(id=1, email="john_doe@example.org", date_of_birth="1990-01-01")

    assert john.date_of_birth == date(1990, 1, 1)


def test_providing_invalid_format_results_in_a_validation_error():
    with pytest.raises(pydantic.ValidationError) as e:
        User(id=1, email="john_doe@example.org", date_of_birth="Jan 1st 1990")

    assert e.value.errors() == [
        {
            "loc": ("date_of_birth",),
            "msg": "invalid date format",
            "type": "value_error.date",
        }
    ]


def test_custom_validation_error():
    with pytest.raises(pydantic.ValidationError) as e:
        User(id=1, email="john_doe@example.com", age=17)

    assert e.value.errors() == [
        {
            "loc": ("age",),
            "msg": "Under-aged users are not allowed.",
            "type": "value_error.under-aged",
        },
    ]


def test_business_user_with_invalid_country():
    with pytest.raises(pydantic.ValidationError) as e:
        BusinessUser(
            id=1,
            email="company@example.org",
            company_name="Example Inc.",
            country="Canada",
        )

    assert e.value.errors() == [
        {
            "loc": ("country",),
            "msg": "Country must be a two-letter code.",
            "type": "value_error",
        }
    ]


def test_business_user_with_invalid_vat_id():
    with pytest.raises(pydantic.ValidationError) as e:
        BusinessUser(
            id=1,
            email="company@example.org",
            company_name="Example Inc.",
            country="BG",
            vat_id="123456789",
        )

    assert e.value.errors() == [
        {
            "loc": ("__root__",),
            "msg": "VAT ID must start with country code BG.",
            "type": "value_error",
        }
    ]
