from flask import abort, jsonify, request


def configure(app):

    @app.errorhandler(400)
    def invalid_data(e):
        return jsonify(error=str(e)), 400

    @app.route("/vowel_count", methods=['POST'])
    def vowel_count():
        json = request.json

        # validate
        try:
            data = json['data']
        except KeyError:
            abort(400, description="Invalid JSON key. Please, use 'data'.")

        is_list = isinstance(data, list)
        is_list_of_strings = all(isinstance(el, str) for el in data) if is_list else False
        if not is_list or not is_list_of_strings:
            abort(400, description='The data must be a list of strings.')

        # process data

        return jsonify(data)
