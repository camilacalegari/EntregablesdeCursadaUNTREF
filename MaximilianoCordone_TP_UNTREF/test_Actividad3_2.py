import requests
import time

""" 
Sitio: Poke Api (https://pokeapi.co/api/v2)

#Caso 1
● Hacer un get a berry/1
● Verificar que el size sea 20
● Verificar que el soil_dryness sea 15
● Verificar que en firmness, el name sea soft 
"""

class TestBerry:
    def test_berry(self):
        response = requests.get("https://pokeapi.co/api/v2/berry/1")    
        assert response.status_code == 200
        data = response.json()
        #print(f"\nDATA BERYY 1:\n{data}")
        assert data["size"] == 20
        assert data["soil_dryness"] == 15
        assert data["firmness"]["name"] == "soft"

""" 
#Caso 2
● Hacer un get a berry/2
● Verificar que en firmness, el name sea super-hard
● Verificar que el size sea mayor al del punto anterior
● Verificar que el soil_dryness sea igual al del punto anterior 
"""
class TestBerry2:
    def test_berry2(self):
        response = requests.get("https://pokeapi.co/api/v2/berry/2")    
        response2 = requests.get("https://pokeapi.co/api/v2/berry/1")    
        
        assert response.status_code == 200
        assert response2.status_code == 200        
        data = response.json()
        data2 = response2.json()
        #print(f"\nDATA BERYY 2:\n {data}, \n --------------------------- \nDATA BERYY 1:\n{data2}")    
        assert data["firmness"]["name"] == "super-hard"
        assert data["size"] > data2["size"]
        assert data["soil_dryness"] == data2["soil_dryness"]
        
""" 
#Caso 3
● Hacer un get a pikachu (https://pokeapi.co/api/v2/pokemon/pikachu/)
● Verificar que su experiencia base es mayor a 10 y menor a 1000
● Verificar que su tipo es “electric” 
"""
class TestPikachu:
    def test_pikachu(self):
        response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu/")    
        assert response.status_code == 200
        data = response.json()
        #print(f"\nDATA PIKACHU:\n{data}")
        assert data["base_experience"] > 10 and data["base_experience"] < 1000
        assert data["types"][0]["type"]["name"] == "electric"