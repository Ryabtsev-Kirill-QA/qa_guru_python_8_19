import jsonschema
import requests
from utils import load_schema
from tests.conftest import BASE_URL


def test_registration_successful():
    schema = load_schema('registration_answer.json')
    email = "eve.holt@reqres.in"
    password = "pistol"

    response = requests.post(f'{BASE_URL}/register', json={
        "email": email,
        "password": password
    })

    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)


def test_registration_unsuccessful():
    wrong_email = "sydney@fife"
    password = "pistol"

    response = requests.post(f'{BASE_URL}/register', json={
        "email": wrong_email,
        "password": password
    })

    assert response.status_code == 400
    assert response.json()['error'] == 'Note: Only defined users succeed registration'
