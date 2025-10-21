# Activar el entorno virtual
.\venv\Scripts\Activate.ps1

# Ejecutar el script de Punto_1/Num_Primo.py
python Punto_1\Num_Primo.py

# Ejecutar el scrit de Punto_2/Ecuacion_Cuadratica.py
python Punto_2\Ecuacion_Cuadratica.py

# Ejecutar las pruebas de Selenium con pytest Punto_3/test_saucedemo.py
pytest .\Punto_3_saucedemo\test_saucedemo.py

# abrir el reporte de saucedemo
start "Punto_3_saucedemo/reporte_saucedemo.html"

# Ejecutar las pruebas de Cypress
npx cypress run

# abrir el reporte de cypress
start "Punto_3_pokeapi/reports/mochawesome/index.html"