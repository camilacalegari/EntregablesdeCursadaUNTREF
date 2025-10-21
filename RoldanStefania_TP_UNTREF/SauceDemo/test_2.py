from selenium.webdriver.common.by import By
import time

def test_checkout_errores(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Agregar todos los productos
    botones = driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")
    for boton in botones:
        boton.click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Stefi")
    driver.find_element(By.ID, "continue").click()
    error1 = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Last Name is required" in error1

    driver.find_element(By.ID, "last-name").send_keys("Roldan")
    driver.find_element(By.ID, "continue").click()
    error2 = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Postal Code is required" in error2
