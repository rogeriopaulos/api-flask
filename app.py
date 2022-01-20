from flasgger import Swagger
from flask import Flask

import views

template = {
  "swagger": "2.0",
  "info": {
    "title": "Count Vowels API",
    "description": "API em Flask que retorna a contagem de vogais a partir de uma lista de strings.",
    "version": "0.0.1"
  },
  "schemes": [
    "http",
  ],
}


def create_app():
    app = Flask(__name__)

    # local apps
    views.configure(app)

    # extensions

    Swagger(app, template=template)
    return app
