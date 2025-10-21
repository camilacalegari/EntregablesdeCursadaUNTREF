from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
import time
import requests

# ======================
# PUNTO 1 DEL TP
# ======================
#Precondición: n debe ser un número natural
def esPrimo():
  #Pedimos el ingreso de un número n
  n = int(input("Ingrese un número para verificar si es primo: "))
  #Caso trivial
  if n == 1:
    return False
  #Casos donde hay que verificar divisores
  i = 2
  while i < n:
    if n % i == 0:
      #Si encontramos un divisor entre 2 y n-1, entonces no es primo
      return False
    i += 1
  return True

# ======================
# PUNTO 2 DEL TP
# ======================
#Precondición: a es un número real distinto de 0
def resolverCuadratica():
  #Pedimos el ingreso de los 3 coeficientes: a, b y c
  a = float(input("Ingrese el coeficiente a, que tiene que ser distinto de 0: "))
  b = float(input("Ingrese el coeficiente b: "))
  c = float(input("Ingrese el coeficiente c: "))
  #Primero determinamos cantidad de raíces
  argumento = b**2 - 4*a*c
  #Luego calculamos las raíces dependiendo del signo del argumento
  if argumento < 0:
    #Caso donde no hay raíces reales
    return print("La ecuación no tiene soluciones reales.")
  elif argumento == 0:
    #Caso de raíz doble, es decir única raíz
    raiz = (-b)/(2*a)
    return print(f"La única raíz de la ecuación es {raiz}.")
  else:
    #Caso de dos raíces
    raiz1 = ((-b)-argumento**(1/2))/(2*a)
    raiz2 = ((-b)+argumento**(1/2))/(2*a)
    return print(f"Las raíces de la ecuación son {raiz1} y {raiz2}.")

# ======================
# PUNTO 3 DEL TP
# ======================

# ======================
# DATOS DE PRUEBA
# ======================
class SauceDemoTestData:
  url = "https://www.saucedemo.com"
  userName = "standard_user"
  password = "secret_sauce"
  name = "Juan"
  lastName = "Perez"
  zip = "1234"

class PokeAPITestData:
  url = "https://pokeapi.co/api/v2"

# ======================
# FIXTURE DEL DRIVER
# ======================
@pytest.fixture
def driver():
  data = SauceDemoTestData()

  #Esto es para aceptar el alerta de contraseña insegura
  chrome_options = Options()
  chrome_options.add_experimental_option("prefs", {
    "profile.password_manager_leak_detection": False
  })

  driver = webdriver.Chrome(options=chrome_options)
  driver.maximize_window()
  driver.get(data.url)

  #Me logueo para todos los tests
  campoUsuario = driver.find_element(By.ID, "user-name")
  campoPassword = driver.find_element(By.ID, "password")
  botonLogin = driver.find_element(By.ID, "login-button")

  campoUsuario.send_keys(data.userName)
  campoPassword.send_keys(data.password)
  botonLogin.click()

  yield driver

  driver.quit()

# ======================
# TESTS
# ======================
class TestSauceDemo():
  #Caso 1
  def test_login_y_ordenar(self, driver):
    data = SauceDemoTestData()

    #Desplegamos el select y presionamos el botón correspondiente
    selectOrden = Select(driver.find_element(By.XPATH, "//select[@data-test='product-sort-container']"))
    selectOrden.select_by_value("lohi")
    time.sleep(1)

    #Verificamos orden de precios
    #Primero: encuentro todos los elementos
    precios = driver.find_elements(By.XPATH, "//div[@data-test='inventory-item-price']")
    #Segundo: los convierto a float y remuevo el símbolo "$"
    listaPrecios = [float(p.text.replace("$", "")) for p in precios]
    #Tercero: "asertamos" orden en la lista
    assert listaPrecios == sorted(listaPrecios), "Los productos no están ordenados por precio."

  #Caso 2
  def test_inputs_vacios(self, driver):
    data = SauceDemoTestData()

    #Agregamos todos los productos al carrito
    #Primero: encuentro todos los botones
    botones = driver.find_elements(By.XPATH, "//div[@class='pricebar']/button")
    #Segundo: los clickeo a todos
    for boton in botones:
      boton.click()
    time.sleep(1)
    
    #Nos dirigimos al carrito
    botonCarrito = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
    botonCarrito.click()
    time.sleep(1)

    #Verifico que el carrito tenga 6 productos
    carrito = driver.find_elements(By.XPATH, "//div[@data-test='inventory-item']")
    assert len(carrito) == 6, "El carrito no tiene 6 productos."

    #Vamos al checkout
    botonCheckout = driver.find_element(By.ID, "checkout")
    botonCheckout.click()
    time.sleep(1)

    #Escribimos el nombre y clickeamos en continuar
    campoNombre = driver.find_element(By.ID, "first-name")
    campoNombre.send_keys(data.name)
    botonContinuar = driver.find_element(By.ID, "continue")
    botonContinuar.click()

    #Verificamos el error
    mensajeError = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert mensajeError.text == "Error: Last Name is required", "El mensaje de error no es correcto."
    time.sleep(1)

    #Escribimos un apellido y clickeamos en continuar
    campoApellido = driver.find_element(By.ID, "last-name")
    campoApellido.send_keys(data.lastName)
    botonContinuar.click()

    #Verificamos el error
    assert mensajeError.text == "Error: Postal Code is required", "El mensaje de error no es correcto."
  
  #Caso 3
  def test_remover_agregar_y_comprar(self, driver):
    data = SauceDemoTestData()
    
    #Agregamos un producto al carrito
    boton = driver.find_element(By.XPATH, "//div[@class='pricebar']/button")
    boton.click()
    time.sleep(1)

    #Nos dirigimos al carrito y lo removemos
    botonCarrito = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
    botonCarrito.click()
    time.sleep(1)
    botonRemove = driver.find_element(By.ID, "remove-sauce-labs-backpack")
    botonRemove.click()
    time.sleep(1)

    #Verificamos que el artículo esté removido
    #Es decir, verificamos que haya un div con la clase "removed_cart_item"
    removidos = driver.find_elements(By.CLASS_NAME, "removed_cart_item")
    assert len(removidos) == 1, "El artículo no fue removido."
    time.sleep(1)

    #Continuamos comprando
    botonContinuar = driver.find_element(By.ID, "continue-shopping")
    botonContinuar.click()
    time.sleep(1)

    #Agregamos los dos primeros productos y volvemos al carrito
    botonesAgregar = driver.find_elements(By.XPATH, "//div[@class='pricebar']/button")
    botonesAgregar[0].click()
    botonesAgregar[1].click()
    time.sleep(1)
    botonCarrito = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
    botonCarrito.click()
    time.sleep(1)

    #Verificamos que hay 2 productos
    productos = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(productos) == 2, "No hay 2 artículos en el carrito."
    time.sleep(1)

    #Vamos al checkout y completamos formulario
    botonCheckout = driver.find_element(By.ID, "checkout")
    botonCheckout.click()
    time.sleep(1)
    campoNombre = driver.find_element(By.ID, "first-name")
    campoApellido = driver.find_element(By.ID, "last-name")
    campoZIP = driver.find_element(By.ID, "postal-code")
    campoNombre.send_keys(data.name)
    campoApellido.send_keys(data.lastName)
    campoZIP.send_keys(data.zip)
    time.sleep(1)

    #Continuamos y finalizamos compra
    botonContinuar = driver.find_element(By.ID, "continue")
    botonContinuar.click()
    time.sleep(1)
    botonFinalizar = driver.find_element(By.ID, "finish")
    botonFinalizar.click()
    time.sleep(1)

    #Verificamos que la compra fue realizada
    mensajeExito = driver.find_element(By.XPATH, "//h2[@data-test='complete-header']")
    assert mensajeExito.text == "Thank you for your order!", "La compra no fue exitosa."

class TestPokeAPI():
  #Caso 1
  def test_berry_1(self):
    APIdata = PokeAPITestData()

    #Hacemos la solicitud
    try:
      req = requests.get(f"{APIdata.url}/berry/1")
      req.raise_for_status()
      data = req.json()
    except requests.exceptions.RequestException as e:
      print(e)
    
    #Asertamos el tamaño
    size = data['size']
    assert size == 20, "El size no es el correcto."

    #Asertamos la sequedad del suelo
    soilDryness = data['soil_dryness']
    assert soilDryness == 15, "La sequedad del suelo no es la correcta."

    #Asertamos la firmeza
    firmness = data['firmness']['name']
    assert firmness == "soft", "La firmeza no es la correcta."

  #Caso 2
  def test_berry_2(self):
    APIdata = PokeAPITestData()

    #Hacemos la solicitud
    try:
      req = requests.get(f"{APIdata.url}/berry/2")
      req.raise_for_status()
      data = req.json()
    except requests.exceptions.RequestException as e:
      print(e)

    #Asertamos la firmeza
    firmness = data['firmness']['name']
    assert firmness == "super-hard", "La firmeza no es la correcta."

    #Asertamos el tamaño
    size = data['size']
    assert size > 20, "El size no es el correcto."

    #Asertamos la sequedad del suelo
    soilDryness = data['soil_dryness']
    assert soilDryness == 15, "La sequedad del suelo no es la correcta."
  
  #Caso 3
  def test_pikachu(self):
    APIdata = PokeAPITestData()

    #Hacemos la solicitud
    try:
      req = requests.get(f"{APIdata.url}/pokemon/pikachu")
      req.raise_for_status()
      data = req.json()
    except requests.exceptions.RequestException as e:
      print(e)
    
    #Asertamos la experiencia base
    baseXP = data['base_experience']
    assert (baseXP < 1000 and baseXP > 10), "La experiencia base no está entre 10 y 1000."

    #Asertamos el tipo
    type = data['types'][0]['type']['name']
    assert type == "electric", "El tipo no es el correcto."
    
