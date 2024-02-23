usuccessful_auth_response_result = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "url": {
            "type": "string"
        },
        "statusCode": {
            "type": "integer"
        },
        "statusMessage": {
            "type": "string"
        },
        "message": {
            "type": "string"
        },
        "stack": {
            "type": "string"
        },
        "data": {
            "type": "object",
            "properties": {
                "res": {
                    "type": "object",
                    "properties": {
                        "error": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "error"
                    ]
                }
            },
            "required": [
                "res"
            ]
        }
    },
    "required": [
        "url",
        "statusCode",
        "statusMessage",
        "message",
        "stack",
        "data"
    ]
}
