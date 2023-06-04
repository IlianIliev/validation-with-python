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

# I. Without any input, validation error is thrown:
# validate({}, schema)

# II. Validating a valid user data
validate({"name": "John", "email": "john@example.org"}, schema)
