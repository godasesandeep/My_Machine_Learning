
# 88) creating setup fixtures & passing class object to the test
# 89) passing command line options to select browser at run time


from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
import pytest
#@pytest.mark.usefixture("setup")

from PageObjects.HomePage import HomePage


class TestOne(BaseClass):
    def test_e2e(self):

        homepage = HomePage(self.driver)
        homepage.shopItems().click()

        
        #self.driver.find_element_by_css_selector("a[href='shop']").click()
        cards = self.driver.find_element_by_css_selector(".card-title a")
        i=-1
        for card in cards:
            i=i+1
            cardText=card.text
            print(cardText)
            if cardText =="Blackberry":
                self.driver.find_element_by_css_selector(".card footer button")[i].click()
        self.driver.find_element_by_css_selector("a[class='btn-primary']").click()
        self.driver.find_element_by_Xpath("//button[@class'btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")

        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_Xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = self.driver.find_element_by_css_selector("[class='alert-success']").text

        assert ("Success! Thank You..!" in textMatch)
        
