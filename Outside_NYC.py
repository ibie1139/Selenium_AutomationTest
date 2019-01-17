import time
import platform
# import unittest
import re
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver #
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
# from datetime import datetime


if platform.system() == 'Windows':
   SPI = webdriver.Chrome(executable_path='./chromedriver.exe')
else:
   SPI = webdriver.Chrome() # Test finished

SPI.get("about:blank")
SPI.maximize_window()
# Above: setUp(self)

SPI.get('https://nycdotsignsstg.net')
SPI.implicitly_wait(8)

try:
   assert SPI.find_element_by_xpath('/html/body/div[2]/div/div/div/div/h2').text == 'Disclaimer'
   print('Assertion for {0} passed successfully.'.format('Disclaimer'))
except AssertionError:
   print("Not the first time.")
# Above: existenceYes(xpath, content)

WebDriverWait(SPI, 6).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/button'))).click()
# Following is the wrong one:
# WebDriverWait(SPI, 5).until(EC.presence_of_element_located(By.XPATH, '/html/body/div[2]/div/div/button')).click()
# locator is a tuple of (by, path), but if without () outside of the tuple, it will be regarded as 2 arguments.

# Maybe no need to assert the following
try:
   assert SPI.find_element_by_xpath('//*[@id="root"]/div/div/button/div').text == 'Load parking signs'
   print('Assertion for {0} passed successfully.'.format('Load parking signs'))
except AssertionError:
   print("Wrong")
# Above: existenceYes(xpath, content)

# to enter address and initiate the search
SPI.find_element_by_xpath('//*[@id="root"]/div/div/header/div[1]').click()
print("Find the input box")
time.sleep(1)
address_input1 = "358 Lafayette St, New York, NY 10012, USA"
address_input2 = "Washington D.C., DC, USA"
address = SPI.find_element_by_xpath('//*[@id="input-id"]')
# address.send_keys('Washington D.C., DC, USA')
address.send_keys(address_input2) 
time.sleep(2)
print("Input Successfully")
address.send_keys(Keys.RETURN)
print("Initiate the search")
time.sleep(3)

try:
   # This is for addresses inside NYC only:
   # element_to_hover_over1 = SPI.find_element_by_xpath(
   #     '//*[@id="root"]/div/div/div[5]/div/div/div[1]') #Address inside NYC
   # This is for addresses inside / outside NYC:
   element_to_hover_over1 = SPI.find_element_by_xpath(
       '//*[@id="root"]/div/div/div[3]/div/div/div[1]') #Address outside NYC
   # element_to_hover_over1 = SPI.find_element_by_xpath(
   #     '//*[@id="root"]/div/div/div[3]/div/div/div[1]') #Address outside NYC
   hover = ActionChains(SPI).move_to_element(element_to_hover_over1)
   hover.perform()
   print(element_to_hover_over1.text)
   assert element_to_hover_over1.text == address_input2
   print("The address is in NYC.")
except AssertionError:
   print('The address is not in NYC.')
finally:
    time.sleep(4)
    SPI.quit()