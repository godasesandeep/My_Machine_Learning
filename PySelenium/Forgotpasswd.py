
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj=Service("D:\Driver1\Chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")

driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
time.sleep(2)

#driver.find_element(By.CSS_SELECTOR,"form div:nth child(2)input").send_keys("Hello@1234")
#driver.find_element(By.CSS_SELECTOR,"#ConfirmPassword").send_keys("Hello@1234")

driver.find_element(By.XPATH,"//input[contains(@class,'form-control ng-untouched ng-pristine ng-invalid')]").send_keys("Hello@1234")
driver.find_element(By.ID,"confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(2)



