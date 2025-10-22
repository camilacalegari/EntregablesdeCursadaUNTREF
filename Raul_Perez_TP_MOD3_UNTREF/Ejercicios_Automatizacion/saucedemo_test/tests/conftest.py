# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Asegúrate de tener ChromeDriver en PATH
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
