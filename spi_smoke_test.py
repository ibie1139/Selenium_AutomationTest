# The following is the python script for smoke test of SPI.
import platform
import random #Add
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains #Add
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re
from pyautogui import press, typewrite, hotkey #Add


class SpiSmokeTestCase(unittest.TestCase):
    def setUp(self):
        if platform.system() == "Windows":
            self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        else:
            self.driver = webdriver.Chrome()
        #TODO - Every test should be run and sends output message pass/fail individually, not as part of a bunch. 
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
        """Send Address '4034 case st'"""
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-id"]'))).send_keys(
            'Washington D.C.') #Outside NYC
        # self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-id"]'))).send_keys(
        #     '358 Lafayette St, New York, NY 10012, USA') #Inside NYC
        time.sleep(2)

    def initiate_search(self):
        """Hit Enter"""
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-id"]'))).send_keys(Keys.ENTER)
        """Wait for results"""
        time.sleep(5)
    
    def address_In_Out_NYC(self):
        """Check whether the address outside NYC get the correct alert message."""
        # This is for addresses inside NYC only:
        # element_to_hover_over1 = SPI.find_element_by_xpath(
        #     '//*[@id="root"]/div/div/div[5]/div/div/div[1]') #Address inside NYC
        # address_input = '358 Lafayette St, New York, NY 10012, USA'
        address_input = 'Washing D.C.'
        try:
            element_to_hover_over1 = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div[3]/div/div/div[1]') #Remember use self.driver, not self
            hover = ActionChains(self.driver).move_to_element(element_to_hover_over1)
            hover.perform()
            print(element_to_hover_over1.text)
            # assert element_to_hover_over1.text == address_input
            # print("The address entered is in NYC.")
        except AssertionError:
            print(element_to_hover_over1.text)
            # print('The address is not in NYC.')
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
        print('The client will move {} steps.'.format(y))
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

    def test_case(self): # This is the test process.
        self.close_disclaimer()
        # self.open_menu_sidebar()
        # self.close_menu_sidebar()
        self.click_input_box()
        self.clear_input_box()
        self.send_address()
        self.initiate_search()
        self.address_In_Out_NYC()
        # self.pan_map()
        # self.open_street_view()
        # self.close_street_view()
        # self.toggle_list()
        # self.toggle_accordion()
        # press('down')
        # time.sleep(2)
        # press('up')
        # self.toggle_list()
        # self.toggle_subtype_menu()
        # self.toggle_subtype_item()
        # self.toggle_subtype_menu()
        # self.toggle_all_item()
        # self.open_download_menu()
        # self.download_geojson()
        # self.open_download_menu()
        # self.download_csv()
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

# print("Now let's start.")

if __name__ == "__main__":
    unittest.main()

# Every Python module has it's __name__ defined and if this is '__main__', it implies that the module is
# being run standalone by the user and we can do corresponding appropriate actions.

# For each test, here, each test method:
# assertEqual() -- check an expected result
# assertTrue(), assertFalse() -- verify a condition
# assertRaises() -- verify a specific exception gets raised
# Use methods above instead of assert statement so the test runner can accumulate all test results and produce a report


#  self.driver.execute_script('mapInstance.state.map.setZoom(20)')
#         time.sleep(2)
#         zoomLevel = self.driver.execute_script('return mapInstance.state.map.getZoom()')
#         print('**********************************************************************') 
#         print("ZOOM: {0}".format(zoomLevel))
#         time.sleep(2)
#         zoomLevel = self.driver.execute_script('return mapInstance.state.map.getZoom()')

# elem = self.driver.find_element_by_xpath('//*[@id="list-view"]/div[1]/div')
# elem.send_keys(Keys.ARROW_DOWN)
# elem2=self.driver.find_element_by_xpath('//*[@id="list-view"]/div[6]/div')
# elem2.send_keys(Keys.ARROW_UP)
# self.toggle_accordion()
# send_keys: not work