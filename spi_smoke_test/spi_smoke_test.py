from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re
from pyautogui import press, typewrite, hotke
import random

class SpiSmokeTestCase(unittest.TestCase):
    def setUp(self):
    #    if platform.system() == "Windows":
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        # else:
        #     self.driver = webdriver.Chrome()
        #TODO - Branching for  different OS, windows should use .exe from root,
        #TODO - In every function, Exception handling
        #TODO - In everyexception pass and fail should provide sensible message
        #TODO - pass message should be green
        #TODO - fail message should be red,( and it should have expected result and received result?)
        self.driver.implicitly_wait(30)
        self.base_url = "https://nycdotsignsstg.net"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://nycdotsignsstg.net/")

    def close_disclaimer(self):
        """ Close Disclaimer """
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.styles_closeIcon__1QwbI"))).click()
        time.sleep(2)

    def open_menu_sidebar(self):
        """Open Menu Sidebar"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/header/button[1]'))).click()
        time.sleep(2)

    def close_menu_sidebar(self):
        """Close Menu Sidebar"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[3]/header/button'))).click()
        time.sleep(2)

    def click_input_box(self):
        """Click the input box"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/header/div[1]'))).click()
        time.sleep(2)

    def clear_input_box(self):
        """Clear Input"""
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-id"]'))).clear()
        time.sleep(2)

    def send_address(self):
        """Send Address '358 Lafayette St, New York'"""
        # self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-id"]'))).send_keys(
        #     'Washington D.C.')
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-id"]'))).send_keys(
        '358 Lafayette St, New York, NY 10012, USA')
        time.sleep(2)

    def initiate_search(self):
        """Hit Enter"""
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-id"]'))).send_keys(Keys.ENTER)
        """Wait for results"""
        time.sleep(8)

    def address_In_Out_NYC(self):
        """Check whether the address outside NYC get the correct alert message."""
        try:
            element_to_hover_over1 = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[1]')
            hover = ActionChains(self.driver).move_to_element(element_to_hover_over1)
            hover.perform()
            print(element_to_hover_over1.text)
            assert element_to_hover_over1.text == '358 Lafayette St, New York, NY 10012, USA'
            print("If the text returned above is an address, then the address entered is in NYC.")
        except AssertionError:
            print('The address is not in NYC.')
        finally:
            time.sleep(4)

    def pan_map(self):
        def pan_direction(self, num, dir):
            while num > 0:
                press(dir)
                time.sleep(1)
                num=num-1
            time.sleep(2)
        self.driver.find_element_by_css_selector('#root > div > div').click()
        y=random.randint(4,6)
        print('The client will pan the map {} times in all directions.'.format(y))
        pan_direction(self, y, 'right')
        pan_direction(self, y, 'left')
        pan_direction(self, y, 'up')
        pan_direction(self, y, 'down')

    def open_street_view(self):
        """Open streetview"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[3]/div[1]'))).click()
        time.sleep(10)

    def close_street_view(self):
        """Close streetview"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="streetViewContainer"]/div[1]'))).click()
        time.sleep(2)

    def toggle_list(self):
        """Toggle List"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[3]/div[3]/div[2]'))).click()
        time.sleep(2)

    def toggle_accordion(self):
        """Toggle Accordion"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list-view"]/div[1]/div'))).click()
        time.sleep(2)

    def toggle_subtype_menu(self):
        """Toggle subtype"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[3]/div[3]/div[1]'))).click()
        time.sleep(2)

    def toggle_subtype_item(self):
        """Toggle subtype item"""
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul.menu.subtype > li:first-child'))).click()
        time.sleep(2)

    def toggle_all_item(self):
        """Toggle subtype item All"""
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul.menu.subtype > li:last-child'))).click()
        time.sleep(3)

    def open_download_menu(self):
        """Open download menu"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[3]/div[3]/div[3]'))).click()
        time.sleep(2)

    def download_geojson(self):
        """Download Geojson"""
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul.menu.downloads > li:first-child'))).click()
        time.sleep(5)

    def download_csv(self):
        """Download CSV"""
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul.menu.downloads > li:last-child'))).click()
        time.sleep(5)

    def open_cyclorama(self):
        """Open Cyclorama"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[3]/div[3]/div[4]'))).click()
        time.sleep(15)

    def close_cyclorama(self):
        """Open Cyclorama"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]'))).click()
        time.sleep(5)

    def clear_results(self):
        """Clear search results"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/header/div[2]'))).click()
        time.sleep(5)

    def test_case(self):
        self.close_disclaimer()
        self.open_menu_sidebar()
        self.close_menu_sidebar()
        self.click_input_box()
        self.clear_input_box()
        self.send_address()
        self.initiate_search()
        self.pan_map()
        self.open_street_view()
        self.close_street_view()
        self.toggle_list()
        self.toggle_accordion()
        self.toggle_accordion()
        self.toggle_list()
        self.toggle_subtype_menu()
        self.toggle_subtype_item()
        self.toggle_subtype_menu()
        self.toggle_all_item()
        self.open_download_menu()
        self.download_geojson()
        self.open_download_menu()
        self.download_csv()
        # self.open_cyclorama()
        # self.close_cyclorama()
        self.driver.execute_script('alert("All test finished")')
        time.sleep(2)


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
