import platform
import os
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER = webdriver.Chrome(executable_path='./drivers_win/chromedriver.exe') if platform.system() == 'Windows' else webdriver.Chrome()


def open_browser_instance(driver, url):
    driver.get("about:blank")
    driver.implicitly_wait(10.0)
    driver.maximize_window()
    driver.get(url)

def teardown(driver):
    try:
        driver.quit()
        print(colored('Browser successfully terminated.\n', 'yellow'))
    except:
        print(colored('Browser could not be closed\n', 'red'))

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def find_element(by, element):
    if by == 'class_name':
        return WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.CLASS_NAME, element)))
    elif by == 'css_selector':
        return WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
    elif by == 'id':
        return WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, element)))
    elif by == 'link_text':
        return WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.LINK_TEXT, element)))
    elif by == 'name':
        return WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.NAME, element)))
    elif by == 'partial_link_text':
        return WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, element)))
    elif by == 'tag_name':
        return WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.TAG_NAME, element)))
    elif by == 'xpath':
        return WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.XPATH, element)))
    else:
        raise Exception("""Wrong option: accepted = class_name, css_selector, id, link_text, name, partial_link_text, tag_name, xpath """)
