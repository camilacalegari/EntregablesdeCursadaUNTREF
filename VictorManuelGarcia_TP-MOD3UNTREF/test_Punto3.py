from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
import time

# Caso Numero 1
def test_ordenar_precios_low_to_high():
  
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")
    time.sleep(2) 

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2) 

    select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    select.select_by_value("lohi")
    time.sleep(2) 

    elementos_precios = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precios = [float(el.text.replace("$", "")) for el in elementos_precios]
    time.sleep(2) 


    driver.quit()

#Caso Numero 2
def test_checkout_validaciones():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    botones_agregar = driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
    for boton in botones_agregar:
        boton.click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    items_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    cantidad_items = len(items_carrito)
    print(f"Cantidad de productos en el carrito: {cantidad_items}")
    assert cantidad_items == 6, f"Se esperaban 6 productos, pero hay {cantidad_items}"

    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    driver.find_element(By.ID, "first-name").send_keys("Victor")
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    mensaje_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    print(f"Mensaje mostrado: {mensaje_error}")
    assert mensaje_error == "Error: Last Name is required", "No se mostró el error esperado para el apellido."

    driver.find_element(By.ID, "last-name").send_keys("Manuel")
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    mensaje_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    print(f"Mensaje mostrado: {mensaje_error}")
    assert mensaje_error == "Error: Postal Code is required", "No se mostró el error esperado para el código postal."

    driver.quit()

#Caso Numero 3
def test_compra_completa():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(text(),'Remove')]").click()
    time.sleep(2)

    items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items) == 0, "El carrito debería estar vacío después de eliminar el artículo"
    print("Carrito vacío correctamente")

    driver.find_element(By.ID, "continue-shopping").click()
    time.sleep(2)

    botones_agregar = driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
    botones_agregar[0].click()
    botones_agregar[1].click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items) == 2, f"Se esperaban 2 productos en el carrito, pero hay {len(items)}"
    print("Dos productos agregados al carrito correctamente")

    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    driver.find_element(By.ID, "first-name").send_keys("Victor")
    driver.find_element(By.ID, "last-name").send_keys("Manuel")
    driver.find_element(By.ID, "postal-code").send_keys("1234")
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    driver.find_element(By.ID, "finish").click()
    time.sleep(2)

    mensaje_final = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert mensaje_final == "Thank you for your order!", "El mensaje final no es el esperado."
    print("Compra completada Correctamente")

    driver.quit()