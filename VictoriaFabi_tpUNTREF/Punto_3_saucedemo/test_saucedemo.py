from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

@pytest.fixture
def setup():    
    driver = webdriver.Chrome() 
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    #  Loguearse como usuario standard_user( reutilizable para los 3 casos)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    
    yield driver
    driver.quit()    


#  CASO 1
class TestFiltroDePrecio:
    def test_filtro_precio(self, setup):
        driver = setup  
        
        #  Ordenar los elementos por “price (low to high)”
        select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))    
        select.select_by_value("lohi")
        time.sleep(5) 

        #  Verificar que los elementos estén ordenados de menor a mayor
        filtro = driver.find_element(By.CLASS_NAME, "active_option")
        assert filtro.text == "Price (low to high)"
        print("Caso 1 completado: Productos ordenados correctamente.")


#  CASO 2
class TestCompraFallida:    
    def test_compra_error(self, setup):
        driver = setup

        #  Incorporar al carrito todos los elementos 
        add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
        for button in add_to_cart_buttons:
            button.click()
            time.sleep(1)  # Espera para ver cada agregado
                
        #  Ir al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)

        #  Verificar que todos los elementos estén en el carrito
        wait = WebDriverWait(driver, 10)  # espera hasta 10 segundos
        cart_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))

        assert len(cart_items) == len(add_to_cart_buttons)

        #  Ir al checkout
        driver.find_element(By.ID, "checkout").click()
        time.sleep(1)

        #  Ingresar nombre y clickear “Continue”
        driver.find_element(By.ID, "first-name").send_keys("Victoria")
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)

        #  Verificar que aparece el error “Error: Last Name is required”
        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert error_message == "Error: Last Name is required"

        #  Ingresar un apellido y clickear “Continue”
        driver.find_element(By.ID, "last-name").send_keys("Fabi")
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)

        #  Verificar que aparece el error “Error: Postal Code is required”
        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert error_message == "Error: Postal Code is required"
        print("Caso 2 completado: Errores de checkout verificados.")


#  CASO 3
class TestCompraExitosa:
    def test_compra_exitosa(self, setup):
        driver = setup
        
        #  Agregar un elemento al carrito
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(1)

        #  Ir al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)

        #  Remover el artículo
        driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
        time.sleep(1)
        
        #  Verificar que no haya artículos agregados
        assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 0

        #  Ir a “Continue Shopping”
        driver.find_element(By.ID, "continue-shopping").click()
        time.sleep(1)

        #  Agregar 2 elementos distintos
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)

        #  Ir al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        
        #  Verificar que los 2 elementos estén en el carrito
        assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 2

        #  Ir al checkout
        driver.find_element(By.ID, "checkout").click()
        time.sleep(1)

        #  Finalizar la compra
        driver.find_element(By.ID, "first-name").send_keys("Victoria")
        driver.find_element(By.ID, "last-name").send_keys("Fabi")
        driver.find_element(By.ID, "postal-code").send_keys("2000")
        driver.find_element(By.ID, "continue").click()
        time.sleep(1)

        driver.find_element(By.ID, "finish").click()
        time.sleep(2)
        
        #  Verificar que la compra fue realizada correctamente
        assert driver.find_element(By.CLASS_NAME, "complete-header").text == "Thank you for your order!"
        print("Caso 3 completado: Compra exitosa verificada.")
