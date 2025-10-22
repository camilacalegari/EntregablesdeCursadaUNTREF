# tests/test_case2.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_cart_and_checkout_errors(driver):
    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

    # Agregar todos los productos al carrito
    add_buttons = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory"))
    )
    for btn in add_buttons:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(btn)).click()
        time.sleep(0.2)  # Pausa breve para ver cada click

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_items = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
    )
    assert len(cart_items) == len(add_buttons)
    time.sleep(1)

    # Checkout sin datos
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Raul")
    driver.find_element(By.ID, "continue").click()

    # Verificar error “Last Name is required”
    error_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container"))
    )
    error = error_element.text
    assert "Last Name is required" in error
    time.sleep(1)

    # Completar apellido y verificar error de postal code
    driver.find_element(By.ID, "last-name").send_keys("Perez")
    driver.find_element(By.ID, "continue").click()
    error_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container"))
    )
    error = error_element.text
    assert "Postal Code is required" in error
    time.sleep(1)
