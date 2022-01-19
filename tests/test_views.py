def test_vowel_count_get_error(app):
    with app.test_client() as client:
        resp = client.get('/vowel_count')
        assert resp.status_code == 405


def test_vowel_count_non_valid_post_data_wrong_format(app):
    with app.test_client() as client:
        resp = client.post(
            '/vowel_count',
            json={'dataset': ['banana', 'apple', 'orange']}
        )
        assert resp.status_code == 400
        assert resp.json.get('error') == "400 Bad Request: Invalid JSON key. Please, use 'data'."


def test_vowel_count_non_valid_post_data_non_list(app):
    with app.test_client() as client:
        resp = client.post('/vowel_count', json={'data': 36})
        assert resp.status_code == 400
        assert resp.json.get('error') == "400 Bad Request: The data must be a list of strings."


def test_vowel_count_non_valid_post_data_list(app):
    with app.test_client() as client:
        resp = client.post(
            '/vowel_count',
            json={'data': ['grape', 1, 2.34]}
        )
        assert resp.status_code == 400
        assert resp.json.get('error') == "400 Bad Request: The data must be a list of strings."


def test_vowel_count_valid(app):
    with app.test_client() as client:
        resp = client.post(
            '/vowel_count',
            json={'data': ['banana', 'apple', 'orange']}
        )
        json_data = resp.get_json()
        expected_response_data = {'banana': 3, 'apple': 2, 'orange': 3}
        assert resp.status_code == 200
        assert json_data == expected_response_data
