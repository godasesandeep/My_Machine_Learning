
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj=Service("D:\Driver1\Chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownspractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")
#driver.find_element(By.XPATH,"//input[contains(@class,'inputs ui-autocomplete-input')]")
time.sleep(2)

countries=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']a")
print(len(countries))
for country in countries:
    if country.text=="India":
        country.click()
        break

assert driver.find_element(By.ID,"autosuggest").get_attribute("value")=="India"