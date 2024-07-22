# Program to verify the Login details of website
from Data import datas
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest

class Test_LoginPage:
   @pytest.fixture
   def booting(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.driver.get(datas.WebData().url)#Launching URL
       self.driver.maximize_window()
       self.action = ActionChains(self.driver)#Creating Objects for Action chains
       self.wait = WebDriverWait(self.driver, 10)  # Explicit wait for 10 seconds
       yield
       self.driver.quit()

   def findElementByXPath(self, xpath):#This method is to locate the xpath
       return self.driver.find_element(by=By.XPATH, value=xpath)

   def fillText(self, locator, textvalue):# this method is to fill text
       element = self.wait.until(ec.presence_of_element_located((By.ID, locator)))
       element.clear()
       element.send_keys(textvalue)

   def test_login(self, booting):
       try:
           #This line to hover over the login button
           login_button = self.driver.find_element(By.XPATH, value=locator.WebLocators().LoginButton)
           self.action.move_to_element(login_button).perform()
           #This line of code enter into the login page
           self.driver.find_element(By.XPATH, value=locator.WebLocators().submit).click()
           #This line of code enters the username
           self.fillText(locator.WebLocators().UsernameLocator, datas.WebData().username)
           #This line of code enters the password
           self.fillText(locator.WebLocators().PasswordLocator, datas.WebData().password)
           self.driver.find_element(By.XPATH, value=locator.WebLocators().checkboxLocator).click()
           # Add assertions to verify login was successful if needed
       except NoSuchElementException as e:
           print(f"Element not found: {e}")

   def test_login2negative(self, booting):
       try:
           # This line to hover over the login button
           login_button = self.driver.find_element(By.XPATH, value=locator.WebLocators().LoginButton)
           self.action.move_to_element(login_button).perform()
           # This line of code enter into the login page
           self.driver.find_element(By.XPATH, value=locator.WebLocators().submit).click()
           # This line of code enters the username
           self.fillText(locator.WebLocators().UsernameLocator, datas.WebData().username)

       except NoSuchElementException as e:
           print(f"Element not found: {e}")
   def test_login3negative(self, booting):
       try:
           # This line to hover over the login button
           login_button = self.driver.find_element(By.XPATH, value=locator.WebLocators().LoginButton)
           self.action.move_to_element(login_button).perform()
           # This line of code enter into the login page
           self.driver.find_element(By.XPATH, value=locator.WebLocators().submit).click()
           # This line of code enters the username
           self.fillText(locator.WebLocators().PasswordLocator, datas.WebData().password)

       except NoSuchElementException as e:
           print(f"Element not found: {e}")



