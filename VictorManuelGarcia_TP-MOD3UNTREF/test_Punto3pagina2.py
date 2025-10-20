import requests

# Caso 1
def test_berry_1():
    url = "https://pokeapi.co/api/v2/berry/1"
    response = requests.get(url)
    data = response.json()
    
    # Verificaciones
    assert data['size'] == 20, f"Expected size 20, got {data['size']}"
    assert data['soil_dryness'] == 15, f"Expected soil_dryness 15, got {data['soil_dryness']}"
    assert data['firmness']['name'] == 'soft', f"Expected firmness 'soft', got {data['firmness']['name']}"
    
# Caso 2
def test_berry_2():
    
    berry_1 = requests.get("https://pokeapi.co/api/v2/berry/1").json()
    
    url = "https://pokeapi.co/api/v2/berry/2"
    response = requests.get(url)
    data = response.json()
    
    # Verificaciones
    assert data['firmness']['name'] == 'super-hard', f"Expected firmness 'super-hard', got {data['firmness']['name']}"
    assert data['size'] > berry_1['size'], f"Expected size greater than {berry_1['size']}, got {data['size']}"
    assert data['soil_dryness'] == berry_1['soil_dryness'], f"Expected soil_dryness {berry_1['soil_dryness']}, got {data['soil_dryness']}"

# Caso 3
def test_pikachu():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
    response = requests.get(url)
    data = response.json()
    
    # Verificaciones
    assert 10 < data['base_experience'] < 1000, f"Expected base_experience between 10 and 1000, got {data['base_experience']}"
    
    tipos = [t['type']['name'] for t in data['types']]
    assert 'electric' in tipos, f"Expected 'electric' type, got {tipos}"