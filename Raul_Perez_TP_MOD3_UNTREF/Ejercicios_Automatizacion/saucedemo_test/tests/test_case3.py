# tests/test_case3.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_add_remove_checkout(driver):
    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

    # Esperar que los productos estén cargados
    products = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory"))
    )

    # Agregar un producto y removerlo
    products[0].click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_items = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
    )
    remove_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "cart_button"))
    )
    remove_button.click()
    assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 0
    time.sleep(1)

    # Agregar 2 productos
    products = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory"))
    )
    products[0].click()
    products[1].click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_items = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
    )
    assert len(cart_items) == 2
    time.sleep(1)

    # Checkout completo
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Raul")
    driver.find_element(By.ID, "last-name").send_keys("Perez")
    driver.find_element(By.ID, "postal-code").send_keys("1000")
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)
    driver.find_element(By.ID, "finish").click()

    # Verificar mensaje final
    complete_text = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text
    assert "THANK YOU FOR YOUR ORDER" in complete_text
    time.sleep(1)


