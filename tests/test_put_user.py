import requests
import pytest
from tests.conftest import BASE_URL


@pytest.mark.parametrize('name', ["neo", "igor", "r2d2"])
def test_rename_user_positive(name):
    user_id = 2
    job = "leader"

    response = requests.put(f'{BASE_URL}/users/{user_id}', json={
        "name": name,
        "job": job
    })

    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job
