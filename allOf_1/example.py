#!/usr/bin/env python3.6

from jsonschema import validate

 # A sample schema, like what we'd get from json.load()
schema = {
    "definitions": {
        "address": {
            "type": "object",
            "properties": {
                "street_address": { "type": "string" },
                "city":           { "type": "string" },
                "state":          { "type": "string" }
            },
            "required": ["street_address", "city", "state"]
        }
    },

    "allOf": [
        {   "$ref": "#/definitions/address" },
        {   "properties": {
            "type": { "enum": [ "residential", "business" ] }
            }
        }
    ]
}

data = {
    "street_address": "1600 Pennsylvania Avenue NW",
    "city": "Washington",
    "state": "DC",
    "type": "business"
}

# If no exception is raised by validate(), the instance is valid.
validate(data, schema)
