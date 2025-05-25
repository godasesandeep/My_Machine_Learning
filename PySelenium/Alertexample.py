
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

name="Ashwini"
service_obj=Service("D:\Driver1\Chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
time.sleep(2)

alert =driver.switch_to.alert
alertText =alert.text
print(alertText)
assert name in alertText
alert.accept()
time.sleep(2)