successful_auth_response_result = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "user": {
            "type": "object",
            "properties": {
                "balance": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "integer"
                        },
                        "fxcode": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "value",
                        "fxcode"
                    ]
                },
                "id": {
                    "type": "integer"
                },
                "ip": {
                    "type": "string"
                },
                "isBot": {
                    "type": "boolean"
                },
                "isStaff": {
                    "type": "boolean"
                },
                "isAdmin": {
                    "type": "boolean"
                },
                "role": {
                    "type": "string"
                }
            },
            "required": [
                "balance",
                "id",
                "ip",
                "isBot",
                "isStaff",
                "isAdmin",
                "role"
            ]
        }
    },
    "required": [
        "user"
    ]
}
