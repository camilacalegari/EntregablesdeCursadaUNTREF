# Este código fue hecho por Matias Nazadek.

# Casos de prueba automatizados del sitio http://www.saucedemo.com/.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time # solamente mientras corría los tests manualmente.
import pytest

# Caso 1:

def test_ordenar_precios_low_to_high():
    # Desactivamos alerta de contraseña insegura de Chrome 
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # El usuario se loguea al sitio como usuario standard user.
    driver.find_element(By.CSS_SELECTOR, '[data-test="username"]').send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()

    # Ordenamos los elementos por “price (low to high)”.
    # Acá me tiraba error de NoSuchElementException asi que usé una espera explícita.
    wait = WebDriverWait(driver, 10)
    elemento = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="product-sort-container"]'))
    )
    select = Select(elemento)
    select.select_by_value("lohi")

    # Verificamos que los elementos estén ordenados.
    precios = [
        float(p.text.replace("$", ""))
        for p in driver.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    ]
    assert precios == sorted(precios), "Los precios no están ordenados de menor a mayor."

    driver.quit()

# Caso 2:

def test_carrito():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # El usuario se loguea al sitio como usuario standard user.
    driver.find_element(By.CSS_SELECTOR, '[data-test="username"]').send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()

    # Incorporamos al carrito todos los elementos.
    # En vez de listar cada uno, selecciono todos los elementos en los que data-test empiece con add-to-cart.
    productos = driver.find_elements(By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
    for producto in productos:
        producto.click()
    #time.sleep(3)

    # Vamos al carrito.
    driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()

    # Verificamos que todos los elementos están en el carrito.
    productos_carrito = driver.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item"]')
    assert len(productos_carrito) == len(productos), "Faltan productos."
    #time.sleep(3)

    # Vamos al checkout.
    driver.find_element(By.CSS_SELECTOR, '[data-test="checkout"]').click()

    # Ingresamos nombre y clickeamos Continue.
    driver.find_element(By.CSS_SELECTOR, '[data-test="firstName"]').send_keys("Matias")
    driver.find_element(By.CSS_SELECTOR, '[data-test="continue"]').click()

    # Verificamos que aparece el error “Error: Last Name is required”.
    error_apellido = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
    assert "Error: Last Name is required" in error_apellido, "El mensaje de error no es correcto."

    # Ingresamos un apellido y clickeamos Continue.
    driver.find_element(By.CSS_SELECTOR, '[data-test="lastName"]').send_keys("Nazadek")
    driver.find_element(By.CSS_SELECTOR, '[data-test="continue"]').click()

    # Verificamos que aparece el error “Error: Postal Code is required”.
    error_cp = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
    assert "Error: Postal Code is required" in error_cp, "El mensaje de error no es correcto."

    driver.quit()

# Caso 3:

def test_checkout():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # El usuario se loguea al sitio como usuario standard user.
    driver.find_element(By.CSS_SELECTOR, '[data-test="username"]').send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()

    # Agregamos un elemento al carrito.
    driver.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]').click()

    # Vamos al carrito.
    driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()

    # Removemos el artículo.
    driver.find_element(By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack"]').click()

    # Verificamos que el sitio no tiene artículos agregados.
    productos_carrito = driver.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item"]')
    assert len(productos_carrito) == 0, "El carrito tiene artículos agregados."
    #time.sleep(3)

    # Vamos a Continue Shopping.
    driver.find_element(By.CSS_SELECTOR, '[data-test="continue-shopping"]').click()

    # Agregamos dos elementos.
    driver.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click()

    # Volvemos al carrito.
    driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()

    # Verificamos que los elementos existen.
    productos_carrito = driver.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item"]')
    assert len(productos_carrito) == 2, "Debería haber dos productos en el carrito."
    #time.sleep(3)

    # Hacemos el checkout.
    driver.find_element(By.CSS_SELECTOR, '[data-test="checkout"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="firstName"]').send_keys("Matias")
    driver.find_element(By.CSS_SELECTOR, '[data-test="lastName"]').send_keys("Nazadek")
    driver.find_element(By.CSS_SELECTOR, '[data-test="postalCode"]').send_keys("CP1234")
    driver.find_element(By.CSS_SELECTOR, '[data-test="continue"]').click()

    # Finalizamos la compra.
    driver.find_element(By.CSS_SELECTOR, '[data-test="finish"]').click()

    # Verificamos que la compra fue realizada.
    mensaje_compra_realizada = driver.find_element(By.CSS_SELECTOR, '[data-test="complete-header"]').text
    assert mensaje_compra_realizada == "Thank you for your order!", "La compra no se completó correctamente."

    driver.quit()
