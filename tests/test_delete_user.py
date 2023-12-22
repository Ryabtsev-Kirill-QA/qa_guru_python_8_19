import requests
from tests.conftest import BASE_URL


def test_delete_user_positive():
    user_id = 2

    response = requests.delete(f'{BASE_URL}/users{user_id}')

    assert response.status_code == 204
    assert response.text == ''
