import time
import platform
import re
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException

# Identify Operating system
# Create an instance of Chrome WeDriver:
if platform.system() == 'Windows':
   SIMS = webdriver.Chrome(executable_path='./chromedriver.exe')
else:
   SIMS = webdriver.Chrome()

SIMS.maximize_window()
# SIMS.set_window_size(1080, 800) -- 2nd way to set
time.sleep(2)
SIMS.get("chrome://settings/")
time.sleep(2)
SIMS.execute_script("chrome.settingsPrivate.setDefaultZoom(0.8);")
time.sleep(3)

# Assertion for Going to the right URL
SIMS.get('http://dotqasimsapp01/users/sign_in') # Test
# SIMS.get('http://dotqasimsapp01.dot.nycnet/users/sign_in')
try:
   assert 'SIMS(QA)' in SIMS.title
   print('Assertion for {0} passed successfully.'.format('SIMS(QA)', 'Dashboard', 'Primary Search', 'Package Manager',
                                                     'Closing Interface', 'Order Detail'))
except AssertionError:
   print("Assertion Error")

# 1.Action for Logging In
user = SIMS.find_element_by_name('user[email]')
user.clear()
user.send_keys('simsnyc.engineer3@gmail.com')
time.sleep(1)
pwd = SIMS.find_element_by_name('user[password]')
pwd.clear()
pwd.send_keys('Welcome1')
time.sleep(1)
sign_in = SIMS.find_element_by_xpath('//*[@id="new_user"]/fieldset/input')
sign_in.send_keys(Keys.RETURN)
# SIMS.find_element_by_partial_link_text("Sign in").click
# SIMS.find_element_by_xpath('//*[@id="new_user"]/fieldset/input').click()
time.sleep(3)

# el = SIMS.find_element_by_name('search_proxy[record_type]')
# for option in el.find_elements_by_tag_name('option'):
#     if option.text == 'Pending Repair':
#         option.click() # select() in earlier versions of webdriver
#         break
# SIMS.execute_script("document.body.style.zoom='zoom 90%'")
# time.sleep(2)


# 2.Search an order:
# SIMS.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[1]/li[2]/a').click()
# SIMS.find_element_by_partial_link_text("Search").click()
SIMS.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar-collapse"]/ul[1]/li[2]/a'))).click()

time.sleep(2)
# SIMS.find_element_by_xpath('//*[@id="new_search_proxy"]/div[7]/div[1]/div[1]/div[5]').click() #Record Type
select = Select(SIMS.find_element_by_id('search_proxy_record_type'))
time.sleep(1)
# select.select_by_visible_text('Pending Sign')
select.select_by_visible_text('Current')
time.sleep(1)

SIMS.find_element_by_xpath('//*[@id="new_search_proxy"]/div[7]/div[1]/div[1]/div[6]').click() #Order Type
order_nbr = SIMS.find_element_by_xpath('//*[@id="search_proxy_order_number"]')
order_nbr.send_keys('C-')
time.sleep(1)
search = SIMS.find_element_by_xpath('//*[@id="form-submit"]')
search.send_keys(Keys.RETURN)
# SIMS.find_element_by_xpath('//*[@id="form-submit"]').click()
time.sleep(2)
print('Execute: {}'.format("Enter criteria and initiate the search."))

try: #This can be very useful everytim go back to the search results
   if ('Too many elements to display on the map.' in SIMS.page_source):
       SIMS.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button').click()
       print('Execute: {}'.format('Too many elements to display on the map.'))
       time.sleep(5)
except NoSuchElementException as e:
   print(e)
finally: #This one will be run no matter an exception is raised or not.
   print("Here are the search results.")


# 3.Click one order
order_number = SIMS.find_element_by_xpath('//*[@id="order_search_results_table"]/tbody/tr[1]/td[13]/a').text
SIMS.find_element_by_xpath(
   '//*[@id="order_search_results_table"]/tbody/tr[1]/td[13]/a').click() # That order links' xpath
print('Execute: Click order {}'.format(order_number))
time.sleep(5)


# 4.Create a pending sign order
   # Difficulty: pop-up window

# 4.1.Action Menu - Create New Sign Order
SIMS.find_element_by_xpath('//*[@id="order-actions"]/div/button').click() # "Actions: Xpath"
# SIMS.find_element_by_xpath('//*[@id="order-actions"]/div/ul/li[1]').click() # "New Sign Order: XPath"
SIMS.find_element_by_partial_link_text('New Sign Order').click() # Use the text, not XPath
time.sleep(2)

# 4.2.Enter infomation into the pop up window
# Click on the pop-up window so that Selenium knows it needs to work on the pop-up window
SIMS.find_element_by_xpath('//*[@id="form-modal"]/div').click()

# Enter 'Recommended By'
SIMS.find_element_by_xpath('//*[@id="new_sign_order"]/fieldset/div[4]/div[1]/div/div').click()
recom = SIMS.find_element_by_xpath('//*[@id="sign_order_recommended_by"]')
recom.send_keys('YY')
time.sleep(1)
SIMS.find_element_by_xpath('//*[@id="create_new_sign_order"]').click()
time.sleep(3)
print('Execute: {}'.format("Create a Pending Sign Order."))


# 5.Navigation back to Current Order Tab and forth to Other Orders' Tabs
SIMS.find_element_by_xpath('//*[@id="view"]/div[4]/div/div/div/div[2]/div/div[2]/div/ul/li[2]/a').click()
time.sleep(2)
print('Execute: {}'.format('Navigation back to Current Order Tab'))


# 6.Order: Sign-Editing
SIMS.find_element_by_xpath(
   '//*[@id="view"]/div[4]/div/div/div/div[2]/div/div[2]/div/ul/li[1]/a').click() # Go back to the pending sign order
time.sleep(2)
pending = SIMS.find_element_by_xpath('//*[@id="view"]/div[4]/div/div/div/div[2]/div/div[2]/div/ul/li[1]/a/b').text
print(pending)
time.sleep(1)
print('Execute: {}'.format('Navigation back to Pending Sign Order Tab'))

SIMS.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

try:
   SIMS.execute_script("window.scrollTo(0, document.body.scrollHeight);")

   # 6.1.Remove a sign
   SIMS.find_element_by_xpath('//*[@id="signs_table"]/tbody/tr[15]/td[16]/i[4]').click()
   time.sleep(1)
   SIMS.find_element_by_xpath('//*[@id="edit-form"]/div[2]/div[3]/button').click()  # Remove
   time.sleep(2)
   SIMS.find_element_by_xpath('//*[@id="signs_table"]/tbody/tr[15]/td[16]/i').click()  # Undo removal
   time.sleep(3)

   # 6.2.Add a new sign above Seq.1
   SIMS.find_element_by_xpath('//*[@id="signs_table"]/tbody/tr[1]/td[16]/i[1]').click()
   time.sleep(2)

   # 6.2.1.Sign ID:
   # The following 3 lines can be made as a function, used repeatedly
#    WebDriverWait.wait.until(EC.element_to_be_clickable((
#        By.XPATH, '//*[@id="edit-form"]/div[4]/div[1]/div[1]/div[1]/div/div'))).click()#Option1
   SIMS.find_element_by_xpath('//*[@id="edit-form"]/div[4]/div[1]/div[1]/div[1]/div/div').click()#Option2
   sign_ID = SIMS.find_element_by_xpath('//*[@id="sign_proxy_sign_standard"]')
   sign_ID.send_keys('R6-1')  # Enter the sign ID
   time.sleep(2)
   # sign_ID.send_keys(Keys.RETURN)
   # Select from Drop Down:
   SIMS.find_element_by_xpath('//*[@id="edit-form"]/div[4]/div[1]/div[1]/div[1]/div/div/ul/li[1]/a').click()
   time.sleep(1)

   # 6.2.2.Location - Direction:
   # location_Dir = SIMS.find_element_by_xpath('//*[@id="sign_proxy_sign_standard"]')
   select = Select(SIMS.find_element_by_id('sign_proxy_direction_from_intersection_type_id'))
   time.sleep(1)
   select.select_by_visible_text('N C')
   time.sleep(1)

   # 6.2.3.Dist From Int:
   SIMS.find_element_by_xpath('// *[ @ id = "edit-form"] / div[4] / div[1] / div[1] / div[3] / div / div').click()
   time.sleep(1)
   dist = SIMS.find_element_by_xpath('//*[@id="sign_proxy_distance_from_intersection"]')
   dist.clear()
   time.sleep(1)
   dist.send_keys('1')  # Enter the sign ID
   time.sleep(2)

   # 6.2.4.Arrow Pts:
   select = Select(SIMS.find_element_by_id('sign_proxy_arrow_direction_type'))
   time.sleep(1)
   select.select_by_visible_text('East')
   time.sleep(1)

   # 6.2.5.Support:
   select = Select(SIMS.find_element_by_id('sign_proxy_support_type'))
   time.sleep(1)
   select.select_by_visible_text('DR')
   time.sleep(1)

   # 6.2.6.Suport Exists
   select = Select(SIMS.find_element_by_id('sign_proxy_support_exists'))
   time.sleep(1)
   select.select_by_visible_text('No')
   time.sleep(1)

   # 6.2.7.Save
   SIMS.find_element_by_xpath('//*[@id="form-submit"]').click()
   time.sleep(5)

except Exception:
   print('Unknown Error')

finally:
   # Cancel the order, create next time:
   SIMS.find_element_by_xpath('//*[@id="order-actions"]/div/button').click()  # Actions menu XPath, again
   time.sleep(1)
   SIMS.find_element_by_partial_link_text('Cancel this order').click()  # Cancel the order
   # From this one, we can tell, sometimes, when the options in the window are different, the XPATH of the elements
   # are different. Thus, find_element_by_xpath is not the only way nor the best way. Use other find_by_... flexibly.
   time.sleep(1)
   SIMS.find_element_by_xpath('//*[@id="confirm_dialog_modal"]/div/div/div[2]/a[2]').click() # Confirm cancelling
   time.sleep(5)
   print('Execute: {}'.format('Cancel the order.'))



# # Drag and drop
# SIMS.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[1]/li[4]/a').click()
# time.sleep(2)
# ip = SIMS.find_element_by_name('search_proxy[order_number]').send_keys('R-') # Generally use this one
# ip = SIMS.find_element_by_name('search_proxy[order_number]').send_keys(pending) #Use this one, if the order is sent to sign shop
# SIMS.find_element_by_xpath('//*[@id="form-submit"]').click()
# time.sleep(5)
# SIMS.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
# SIMS.find_element_by_xpath('//*[@id="package_toolbar"]/div/div[1]').click()
# time.sleep(2)
# #
# print("FINDING the source")
# source_element = SIMS.find_element_by_xpath('//*[@id="order_search_results_table"]/tbody/tr[3]')
# print("FINDING the drop target")
# dest_element = SIMS.find_element_by_css_selector('.drop-target.panel.panel-success.ui-droppable')
# print("Dropping")
# ActionChains(SIMS).drag_and_drop(source_element, dest_element).perform()
#
time.sleep(10)
# SIMS.quit()

# orderNbr = SIMS.find_element_by_id('search_text')
# orderNbr.send_keys('C-00474404')
# orderNbr.send_keys(Keys.RETURN)