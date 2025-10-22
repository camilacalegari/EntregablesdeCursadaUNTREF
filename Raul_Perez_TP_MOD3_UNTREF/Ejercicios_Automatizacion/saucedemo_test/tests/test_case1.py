# tests/test_case1.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_sort_price_low_to_high(driver):
    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

    # Esperar que los precios estén visibles
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price"))
    )

    # Ordenar por precio (low to high)
    select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    select.select_by_value("lohi")
    time.sleep(1)

    # Verificar orden de precios
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices_float = [float(p.text.replace("$", "")) for p in prices]
    assert prices_float == sorted(prices_float)
    time.sleep(1)

