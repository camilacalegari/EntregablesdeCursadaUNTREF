from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@pytest.fixture
def setup():    
    driver =  webdriver.Chrome() 
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    yield driver
    driver.quit()    
    
""" 
#Caso 1: 
● El usuario se loguea al sitio como usuario standard user
● Ordenar los elementos por “price (low to high)”
● Verificar que los elementos estén ordenados de menor a mayor 
"""
class TestFiltroDePrecio:
    def test_filtro_precio(self, setup):
        # Traer el fixture
        driver = setup  
        
        # Seleccionar "Price (low to high)" en el filtro
        select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))    
        select.select_by_value("lohi")
        
        # Validar que se encuentre seleccionado el filtro
        filtro = driver.find_element(By.CLASS_NAME,"active_option")
        assert filtro.text == "Price (low to high)"       

""" 
#Caso 2:
● El usuario se loguea al sitio como usuario standard user
● Incorporar al carrito todos los elementos
● Ir al carrito
● Verificar que todos los elementos estén en el carrito
● Ir al checkout
● Ingresar nombre y clickear “Continue”
● Verificar que aparece el error “Error: Last Name is required”
● Ingresar un apellido y clickear “Continue”
● Verificar que aparece el error “Error: Postal Code is required” 
"""
class TestCompraFallida:    
    def test_compra_error(self, setup):
        # Trear el fixture
        driver = setup

        # Incorporar al carrito todos los elementos del home
        add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
        for button in add_to_cart_buttons:
            button.click()
                
        # Ir al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Verificar que todos los elementos estén en el carrito
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")        
        assert len(cart_items) == len(add_to_cart_buttons)

        # Ir al checkout
        driver.find_element(By.ID, "checkout").click()

        # Ingresar nombre y clickear “Continue”
        driver.find_element(By.ID, "first-name").send_keys("Maxi")
        driver.find_element(By.ID, "continue").click()

        # Verificar que aparece el error “Error: Last Name is required”
        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert error_message == "Error: Last Name is required"

        # Ingresar un apellido y clickear “Continue”
        driver.find_element(By.ID, "last-name").send_keys("Cordone")
        driver.find_element(By.ID, "continue").click()

        # Verificar que aparece el error “Error: Postal Code is required”
        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert error_message == "Error: Postal Code is required"

""" 
#Caso 3
● El usuario se loguea al sitio como usuario standard user
● Agregar un elemento al carrito
● Ir al carrito
● Remover el artículo
● Verificar que el sitio no tiene artículos agregados
● Ir a “Continue Shopping”
● Agregar 2 elementos
● Ir al carrito
● Verificar que los elementos existan
● Hacer el checkout
● Finalizar la compra
● Verificar que la compra fue realizada 
"""
class TestCompraExitosa:
    def test_compra_exitosa(self, setup):
        # Traer el fixture
        driver = setup
        
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID,"remove-sauce-labs-backpack").click()
        
        # Verficiar que se haya eliminado el item
        assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 0
        driver.find_element(By.ID,"continue-shopping").click()
        driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)").click()
        driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # Verificar que se encuentren los 2 items en el carrito
        assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 2
        driver.find_element(By.ID,"checkout").click()
        driver.find_element(By.ID,"first-name").send_keys("Maxi")
        driver.find_element(By.ID,"last-name").send_keys("Cordone")
        driver.find_element(By.ID,"postal-code").send_keys("1234")
        driver.find_element(By.ID,"continue").click()
        driver.find_element(By.ID,"finish").click()
        
        # Verificar que se haya realizado la compra
        assert driver.find_element(By.CLASS_NAME, "complete-header").text == "Thank you for your order!"