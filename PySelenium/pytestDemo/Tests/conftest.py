
import pytest
from selenium import webdriver
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="D:\Driver1\Chromedriver.exe")
    driver.get("https://qaclickacademy.github.io/protocommerce")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
