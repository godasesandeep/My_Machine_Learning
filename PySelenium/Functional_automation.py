
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
service_obj=Service("D:\Driver1\Chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count >0
for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
time.sleep(2)
#Sum validation
prices=driver.find_elements(By.XPATH,"//tbody/tr/td[5] /p")
sum=0
for price in prices:
    sum=sum+int(price.text)
print(sum)
totalAmount=int(driver.find_element(By.CSS_SELECTOR,'.totAmt').text)
print(totalAmount)
assert sum==totalAmount