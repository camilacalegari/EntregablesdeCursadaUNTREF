from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_ordenar_por_precio(driver):
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Ordenar por precio (low to high)
    select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    select.select_by_visible_text("Price (low to high)")
    time.sleep(1)

    # Verificar orden
    precios = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precios_float = [float(p.text.replace("$", "")) for p in precios]
    assert precios_float == sorted(precios_float), "❌ Los productos no están ordenados correctamente"
