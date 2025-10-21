import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()  # si usás ChromeDriver en PATH no hace falta ruta
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
