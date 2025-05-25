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
driver.find_element(By.XPATH,"//button[@class='search-button']").click()
time.sleep(4)
web_elements=driver.find_elements(By.XPATH,"//div[@class='product']")
num=len(web_elements)
actual_lst=["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
web_lst=[]
if num==3:
    print("Number of element is ",num)
    for element in web_elements:
        ber_name=element.find_element(By.XPATH,"h4").text
        web_lst.append(ber_name)
assert web_lst==actual_lst
for element in web_elements:
        element.find_element(By.XPATH,"div/button").click()
time.sleep(5)
total_price=0
for element in web_elements:
        price=element.find_element(By.XPATH,"p").text
        total_price =total_price+int(price)

print("Total Price is ",total_price)

time.sleep(5)
#assert total_price==388
#driver.find_element(By.CSS_SELECTOR,"img[alt='cart']").click()
#driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT')]").click()
#driver.find_element(By.CSS_SELECTOR,".promocode").send_keys("SandeepAshwini")
#driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
#time.sleep(5)
#print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
       
