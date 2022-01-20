vowel_count_specs = {
    "produces": [
        "application/json",
    ],
    "parameters": [
        {
            "name": "data",
            "in": "body",
            "required": True,
            "type": "object",
            "schema": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
        }
    ],
    "responses": {
        "200": {
            "description": "Uma lista de strings (palavras)",
            "schema": {
                "type": "object",
                "items": {
                    "type": "object"
                }
            }
        }
    }
}
