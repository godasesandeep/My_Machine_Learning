from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
service_obj=Service("D:\Driver1\Chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(1)

results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count >0
for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
driver.find_element(By.XPATH,"//input[contains(@class,'promoCode')]").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[contains(@class,'promoBtn')]").click()

time.sleep(5)