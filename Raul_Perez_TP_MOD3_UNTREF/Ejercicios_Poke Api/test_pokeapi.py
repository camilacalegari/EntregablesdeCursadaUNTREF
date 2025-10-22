import requests

# --- Caso 1 ---
def test_berry_1():
    url = "https://pokeapi.co/api/v2/berry/1"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()

    # Verificaciones
    assert data["size"] == 20, f"El size esperado era 20, pero fue {data['size']}"
    assert data["soil_dryness"] == 15, f"Soil dryness esperado 15, pero fue {data['soil_dryness']}"
    assert data["firmness"]["name"] == "soft", f"Firmness esperado 'soft', pero fue {data['firmness']['name']}"


# --- Caso 2 ---
def test_berry_2():
    url_berry1 = "https://pokeapi.co/api/v2/berry/1"
    url_berry2 = "https://pokeapi.co/api/v2/berry/2"

    berry1 = requests.get(url_berry1).json()
    berry2 = requests.get(url_berry2).json()

    # Verificaciones
    assert berry2["firmness"]["name"] == "super-hard", f"Firmness esperado 'super-hard', pero fue {berry2['firmness']['name']}"
    assert berry2["size"] > berry1["size"], f"El size de berry2 ({berry2['size']}) no es mayor que berry1 ({berry1['size']})"
    assert berry2["soil_dryness"] == berry1["soil_dryness"], f"Soil dryness distinto: berry1={berry1['soil_dryness']}, berry2={berry2['soil_dryness']}"


# --- Caso 3 ---
def test_pikachu():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()

    # Experiencia base
    base_exp = data["base_experience"]
    assert 10 < base_exp < 1000, f"Experiencia fuera de rango: {base_exp}"

    # Tipo
    tipos = [t["type"]["name"] for t in data["types"]]
    assert "electric" in tipos, f"Tipos esperados: 'electric', pero se obtuvo {tipos}"
