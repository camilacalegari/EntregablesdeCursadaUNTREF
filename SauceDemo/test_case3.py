from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_flujo_compra(driver):
    """Caso 3: Flujo completo de compra"""
    driver.get("https://www.saucedemo.com/")

    # 🔹 Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 🔹 Agregar y remover un producto
    driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, ".cart_button").click()
    assert not driver.find_elements(By.CLASS_NAME, "cart_item"), "❌ El carrito debería estar vacío"

    driver.find_element(By.ID, "continue-shopping").click()

    # 🔹 Agregar dos productos
    driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")[0].click()
    driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")[1].click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items) == 2, "❌ No se agregaron correctamente los dos productos"

    # 🔹 Checkout y completar datos
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Stefi")
    driver.find_element(By.ID, "last-name").send_keys("Roldan")
    driver.find_element(By.ID, "postal-code").send_keys("1663")
    driver.find_element(By.ID, "continue").click()

    # 🔹 Esperar a que la página de summary cargue
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout_summary_container"))
    )

    # 🔹 Esperar a que el botón Finish sea clickeable y hacer click
    finish_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    )
    finish_button.click()

    # 🔹 Verificar confirmación de compra
    confirmacion = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text

    assert "THANK YOU" in confirmacion.upper(), "❌ La compra no se completó correctamente"
