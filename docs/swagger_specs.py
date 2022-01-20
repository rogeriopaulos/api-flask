vowel_count_specs = {
    "produces": [
        "application/json",
    ],
    "parameters": [
        {
            "name": "data",
            "description": "Recebe um array (lista) de strings",
            "in": "body",
            "required": True,
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
            "description": "Retorna a contagem de vogais de cada string recebida",
            "schema": {
                "type": "object",
                "properties": {
                    "string": {
                        "type": "integer"
                    }
                }
            }
        },
        "400": {
            "description": "Bad Request: Os dados informados devem ser uma lista de strings.",
        }
    }
}
