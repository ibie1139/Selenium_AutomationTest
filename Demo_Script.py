from selenium import webdriver #Must: import ‘webdriver’ library
from selenium.webdriver.common.action_chains import ActionChains

# These modules enables waits, Implicit and Explicit Waits.
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException

# To Detect which operating system is running
import platform 

from time import sleep

# Create an instance of ChromeDriver
if platform.system() == 'Windows':
   SPI = webdriver.Chrome(
       executable_path='./chromedriver.exe')
else:
   SPI = webdriver.Chrome()

# Open the browser
SPI.get("about:blank")
SPI.maximize_window()

# Enter SPI URL and wait the page loading
SPI.get('https://nycdotsignsstg.net')
SPI.implicitly_wait(8) # Seconds

# Assert Disclaimer Exists
try:
   assert SPI.find_element_by_xpath(
       '/html/body/div[2]/div/div/div/div/h2').text == 'Disclaimer'
   print('Assertion for {0} passed successfully.'.format('Disclaimer'))
except AssertionError:
   print("Assertion Error.")

# Close Disclaimer
WebDriverWait(SPI, 5).until(
    EC.presence_of_element_located((
        By.XPATH, '/html/body/div[2]/div/div/button'))).click()

# Enter Address and initiate the search


WebDriverWait(SPI, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/div/header/div[1]'))
        ).click()

# SPI.find_element_by_xpath('//*[@id="root"]/div/div/header/div[1]').click()
print("Find the input box")
time.sleep(1)


address_input1 = "Washington D.C., DC, USA"
address = SPI.find_element_by_xpath('//*[@id="input-id"]')
address.send_keys(address_input1) 
time.sleep(1)
print("Input Successfully")
address.send_keys(Keys.RETURN)
print("Initiate the search")
time.sleep(3)

# Get Outside-NYC Error Message

try:
   element_to_hover_over1 = SPI.find_element_by_xpath(
       '//*[@id="root"]/div/div/div[3]/div/div/div[1]')
   hover = ActionChains(SPI).move_to_element(element_to_hover_over1)
   hover.perform()
   print(element_to_hover_over1.text)
   assert element_to_hover_over1.text == address_input1
except AssertionError:
   print('The address is not in NYC.')
finally:
    time.sleep(4)
    
    
    
SPI.quit()