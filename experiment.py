# import inspect

# def whoami(): 
#     frame = inspect.currentframe()
#     return inspect.getframeinfo(frame).function

# def foo():
#     print(whoami())

# foo()

# # Print the function name.
# def close_disclaimer(self):
#         """ Close Disclaimer """
#         try:
#             frame = inspect.currentframe()
#             self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.styles_closeIcon__1QwbI"))).click()
#             # frame = inspect.currentframe()
#             # pass_message(frame)
#             print('Test {} pass.'.format(inspect.getframeinfo(frame).function))#Get function name and print.
#         # print('Test {} pass.'.format(close_disclaimer.__name__))
#         except AssertionError:
#             print("Closing disclaimer failed.")

# # Use Javascript to zoom in and out, and get the zoom level:
# self.driver.execute_script('mapInstance.state.map.setZoom(20)')
# time.sleep(2)
# zoomLevel = self.driver.execute_script('return mapInstance.state.map.getZoom()')
# print('**********************************************************************') 
# print("ZOOM: {0}".format(zoomLevel))
# time.sleep(2)
# zoomLevel = self.driver.execute_script('return mapInstance.state.map.getZoom()')

# # Navigating: find_element_by_... is attribute of the object "driver", not attribute of the testCase:
# elem = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/div')
#         elem.send_keys(Keys.ARROW_DOWN)

# from pyautogui import press, typewrite, hotkey

# # press('a')
# # press('/')
# # typewrite('Arrow')
# # hotkey('Ctrl','w')
# # hotkey('shift','w')
# import random
# # for x in range(1):
# y=random.randint(5,10)
# print(y)

# # Try whether we can pass a string to a function:
# def to_string(dir):
#     print(dir)
# to_string('right')



# define the Vehicle class and formatting--color:
import sys
from termcolor import colored, cprint
class Vehicle:
   name = ""
   kind = "car"
   color = ""
   value = 100.00
   def description(self):
       desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
       return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(colored(car1.description(),'yellow'))
print(car2.description())

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')