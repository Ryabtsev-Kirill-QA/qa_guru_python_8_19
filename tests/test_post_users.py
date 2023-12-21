import jsonschema
import requests
from utils import load_schema
from tests.conftest import BASE_URL


def test_create_user_positive():
    schema = load_schema('created_user.json')
    name = "morpheus"
    job = "leader"

    response = requests.post(f'{BASE_URL}/users', json={
        "name": name,
        "job": job
    })

    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    jsonschema.validate(response.json(), schema)
