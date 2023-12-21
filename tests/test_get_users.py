import jsonschema
import requests
from utils import load_schema
from tests.conftest import BASE_URL


def test_get_list_of_users_successfully():
    schema = load_schema('list_users.json')
    page_id = 2

    response = requests.get(f'{BASE_URL}/users?page={page_id}')

    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)


def test_get_single_user_successfully():
    schema = load_schema("single_user.json")
    user_id = 2
    user_email = "janet.weaver@reqres.in"

    response = requests.get(f'{BASE_URL}/users/{user_id}')

    assert response.status_code == 200
    assert response.json()['data']['email'] == user_email
    jsonschema.validate(response.json(), schema)


def test_get_single_user_not_found():
    user_id = 23

    response = requests.get(f'{BASE_URL}/users/{user_id}')

    assert response.status_code == 404
