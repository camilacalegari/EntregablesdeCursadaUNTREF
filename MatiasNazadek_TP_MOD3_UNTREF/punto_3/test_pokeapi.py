# Este código fue hecho por Matias Nazadek.

# Casos de prueba automatizados del sitio https://pokeapi.co/api/v2.

import requests

# Caso 1:

def test_berry_1():
    # Hacemos un get a berry/1.
    response = requests.get("https://pokeapi.co/api/v2/berry/1")

    # Verificamos que el size sea 20.
    assert response.json()["size"] == 20, "Size incorrecto."

    # Verificamos que el soil_dryness sea 15.
    assert response.json()["soil_dryness"] == 15, "Soil dryness incorrecto."

    # Verificamos que en firmness, el name sea soft.
    assert response.json()["firmness"]["name"] == "soft", "Firmness incorrecto."

def test_berry_2():
    # Hacemos un get a berry/2 y guardamos el JSON en data.
    response = requests.get("https://pokeapi.co/api/v2/berry/2")
    data = response.json()

    # Verificamos que en firmness, el name sea super-hard.
    assert data["firmness"]["name"] == "super-hard", "Name incorrecto."

    # Verificamos que el size sea mayor al del punto anterior (berry/1).
    response_berry_1 = requests.get("https://pokeapi.co/api/v2/berry/1")
    data_berry_1 = response_berry_1.json()
    assert data["size"] > data_berry_1["size"], "Size no es mayor a berry/1."

    # Verificamos que el soil_dryness sea igual al del punto anterior.
    assert data["soil_dryness"] == data_berry_1["soil_dryness"], "Soil dryness no es igual a berry/1"

def test_pikachu():
    # Hacemos un get a Pikachu y guardamos el JSON en data.
    r = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu/")
    data = r.json()

    # Verificamos que su experiencia base es mayor a 10 y menor a 1000.
    assert data["base_experience"] > 10, "Base experience no es mayor a 10"
    assert data["base_experience"] < 1000, "Base experience no es menor a 1000"

    # Verificamos que su tipo es “electric”.
    assert data["types"][0]["type"]["name"] == "electric", "Type incorrecto."

