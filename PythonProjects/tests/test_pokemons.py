import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "b3d0ee6c1c050bc12b69f93647ee6620"
HEADER = {"Content-Type" : "application/json", "trainer_token": TOKEN}
TRAINER_ID = '28618'

def test_status_code():
    response = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response(): 
    response_get = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == "Ebabelno"


@pytest.mark.parametrize("key, value", [("trainer_name", 'Ebabelno'), ('trainer_id', TRAINER_ID), ('level', '5')])
def test_parametrize(key, value): 
    response_parametrize = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value 