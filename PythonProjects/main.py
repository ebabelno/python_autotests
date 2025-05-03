import requests 

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "b3d0ee6c1c050bc12b69f93647ee6620"
HEADER = {"Content-Type" : "application/json", "trainer_token": TOKEN}

body_create = {
    "name": "Рачик",
    "photo_id": 1
}

response_create = requests.post(url = f"{URL}/pokemons", headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()["id"]

body_edit = {
    "pokemon_id": str(pokemon_id),
    "name": "Якубович",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": str(pokemon_id)
}

response_edit = requests.put(url = f"{URL}/pokemons", headers = HEADER, json = body_edit)
print(response_edit.text) 

response_catch = requests.post(url = f"{URL}/trainers/add_pokeball", headers = HEADER, json = body_catch)
print(response_catch.text) 