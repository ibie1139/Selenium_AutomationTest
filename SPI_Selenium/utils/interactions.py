#!/usr/bin/python

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init
from termcolor import colored
init()

def click(driver, xpath):
  try:
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, xpath))
    ).click()
  except TimeoutException:
    print("Test timeout")
  time.sleep(3)



def submit_form(driver, xpath, form_content):
  form = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, xpath))
  )
  form.send_keys(form_content)
  form.send_keys(Keys.RETURN)
  time.sleep(5)



def check_existence(driver, xpath, content):
  try:
    assert driver.find_element_by_xpath(xpath).text == content
    print(colored("Assertion for {0} Passed Successfully.".format(content), 'green'))
  except AssertionError:
    print(colored("Assertion for {0} Failed. {0} Text could not be found".format(content), 'white', 'on_red'))


def check_non_existence(driver, xpath, content):
  try:
    assert driver.find_element_by_xpath(xpath).text != content
    print(colored("Assertion for {0} Passed Successfully.".format(content), 'green'))
  except AssertionError:
    print(colored("Assertion for {0} Failed. {0}".format(content), 'white', 'on_red'))
