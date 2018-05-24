#!/usr/bin/env python3.6

from jsonschema import validate

 # A sample schema, like what we'd get from json.load()
schema = {
    "type": "string",
    "enum": ["red", "amber", "green", None, 42] # Python: None, JSON: null
}

# If no exception is raised by validate(), the instance is valid.
validate("red", schema)
# validate(None, schema)
# validate(3, schema)
