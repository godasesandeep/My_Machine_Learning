
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
import time


service_obj=Service("D:\Driver1\Chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
time.sleep(5)
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action .move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
