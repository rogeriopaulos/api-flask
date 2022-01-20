from flasgger import swag_from
from flask import abort, jsonify, request

from docs.swagger_specs import vowel_count_specs
from utils import count_vowels


def configure(app):

    @app.errorhandler(400)
    def invalid_data(e):
        return jsonify(error=str(e)), 400

    @app.route("/vowel_count", methods=['POST'])
    @swag_from(vowel_count_specs)
    def vowel_count():
        """Retorna a contagem de vogais de cada palavra a partir de uma lista de string
        """
        # json = request.json
        data = request.json

        # # validate
        # try:
        #     data = json['data']
        # except KeyError:
        #     abort(400, description="Invalid JSON key. Please, use 'data'.")

        is_list = isinstance(data, list)
        is_list_of_strings = all(isinstance(el, str) for el in data) if is_list else False
        if not is_list or not is_list_of_strings:
            abort(400, description='The data must be a list of strings.')

        # process data
        response_data = {item: count_vowels(item) for item in data}

        return jsonify(response_data)
