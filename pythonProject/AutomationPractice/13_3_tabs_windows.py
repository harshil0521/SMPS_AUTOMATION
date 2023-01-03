from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
#
# driver.find_element(By.LINK_TEXT, "Register").send_keys(Keys.CONTROL+Keys.ENTER)

# Opens new tab and move to the new tab
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window("tab")
# driver.get("https://demo.nopcommerce.com/")

# Opens new browser window and move to the new browser window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window("window")
driver.get("https://demo.nopcommerce.com/")
