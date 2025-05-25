from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj=Service('D:\Driver1/chromedriver.exe')

driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
time.sleep(2)
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Ashwini")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(1)
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message
time.sleep(7)
