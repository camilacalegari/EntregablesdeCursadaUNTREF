import requests

def test_caso1():
    url = "https://pokeapi.co/api/v2/berry/1"
    response = requests.get(url)
    assert response.status_code == 200, f"Error HTTP {response.status_code}"
    data = response.json()
    assert data["size"] == 20, f"'size' incorrecto: {data['size']}"
    assert data["soil_dryness"] == 15, f"'soil_dryness' incorrecto: {data['soil_dryness']}"
    assert data["firmness"]["name"] == "soft", f"'firmness.name' incorrecto: {data['firmness']['name']}"

def test_caso2():
    url_berry1 = "https://pokeapi.co/api/v2/berry/1"
    response1 = requests.get(url_berry1)
    assert response1.status_code == 200, f"Error HTTP {response1.status_code}"
    berry1 = response1.json()
    size_berry1 = berry1["size"]
    soil_dryness_berry1 = berry1["soil_dryness"]

    url_berry2 = "https://pokeapi.co/api/v2/berry/2"
    response2 = requests.get(url_berry2)
    assert response2.status_code == 200, f"Error HTTP {response2.status_code}"
    berry2 = response2.json()
    assert berry2["firmness"]["name"] == "super-hard", f"'firmness.name' incorrecto: {berry2['firmness']['name']}"
    assert berry2["size"] > size_berry1, f"'size' no es mayor: {berry2['size']} <= {size_berry1}"
    assert berry2["soil_dryness"] == soil_dryness_berry1, (
        f"'soil_dryness' distinto: {berry2['soil_dryness']} != {soil_dryness_berry1}"
    )

def test_caso3():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
    response = requests.get(url)
    assert response.status_code == 200, f"Error HTTP {response.status_code}"
    data = response.json()
    base_exp = data["base_experience"]
    assert 10 < base_exp < 1000, f"base_experience fuera de rango: {base_exp}"
    types = [t["type"]["name"] for t in data["types"]]
    assert "electric" in types, f"Tipo 'electric' no encontrado. Tipos actuales: {types}"

