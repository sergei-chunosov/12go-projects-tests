successful_search_result = {
    "$schemas": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    # "additionalProperties": False,
    "properties": {
        "type": {
            "type": "string"
        },
        "trip_id": {
            "type": "string"
        },
        "official_id": {
            "type": "string"
        },
        "from": {
            "type": "integer"
        },
        "to": {
            "type": "integer"
        },
        "dep_time": {
            "type": "string"
        },
        "arr_time": {
            "type": "string"
        },
        "duration": {
            "type": "integer"
        },
        "class": {
            "type": "integer"
        },
        "operator": {
            "type": "integer"
        },
    },
    "required": [
        "type",
        "trip_id",
        "official_id",
        "from",
        "to",
        "dep_time",
        "arr_time",
        "duration",
        "class",
        "operator"
    ]
}
