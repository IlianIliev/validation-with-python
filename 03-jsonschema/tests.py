import jsonschema
import pytest
from jsonschema import validate


schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "age": {"type": "integer"},
        "role": {"type": "string", "enum": ["admin", "user"]},
    },
    "required": ["name", "email"],
}


def test_without_any_input_it_raises_validation_error():
    with pytest.raises(jsonschema.ValidationError) as e:
        validate({}, schema)

    assert e.value.message == "'name' is a required property"


def test_validating_a_valid_user():
    assert validate({"name": "John", "email": "john@example.org"}, schema) is None
