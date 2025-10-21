from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest

# caso1
def test_caso1():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    elemento = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(elemento)
    select.select_by_value("lohi")  
    time.sleep(2)

    precios_elementos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precios = [float(p.text.replace("$", "")) for p in precios_elementos]

    assert precios == sorted(precios), "Los precios no se ordenaron correctamente"
    driver.quit()

# caso2
def test_caso2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    productos = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bike-light",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-fleece-jacket",
        "add-to-cart-sauce-labs-onesie",
        "add-to-cart-test.allthethings()-t-shirt-(red)"
    ]
    for producto in productos:
        driver.find_element(By.ID, producto).click()
    time.sleep(2)

    driver.find_element(By.ID, "shopping_cart_container").click()
    carrito = driver.find_element(By.CSS_SELECTOR, "div.cart_list")
    items = carrito.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items) > 0, "El carrito está vacío"

    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Guille")
    driver.find_element(By.ID, "continue").click()

    mensaje_error1 = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Error: Last Name is required" in mensaje_error1, f"Mensaje inesperado: {mensaje_error1}"

    driver.find_element(By.ID, "last-name").send_keys("Oliva")
    driver.find_element(By.ID, "continue").click()

    mensaje_error2 = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Error: Postal Code is required" in mensaje_error2, f"Mensaje inesperado: {mensaje_error2}"

    driver.quit()

# caso3
def test_caso3():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "shopping_cart_container").click()
    time.sleep(5)
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    carrito = driver.find_element(By.CSS_SELECTOR, "div.cart_list")
    items = carrito.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items) == 0, f"Se esperaba carrito vacío, pero hay {len(items)} producto(s)"

    driver.find_element(By.ID, "continue-shopping").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    driver.find_element(By.ID, "shopping_cart_container").click()
    carrito = driver.find_element(By.CSS_SELECTOR, "div.cart_list")
    items = carrito.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items) > 0, "El carrito debería tener productos, pero está vacío"

    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Guille")
    driver.find_element(By.ID, "last-name").send_keys("Oliva")
    driver.find_element(By.ID, "postal-code").send_keys("1714")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()

    mensaje_confirmacion = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you for your order!" in mensaje_confirmacion, f"Error al completar la compra: {mensaje_confirmacion}"

    driver.quit()
