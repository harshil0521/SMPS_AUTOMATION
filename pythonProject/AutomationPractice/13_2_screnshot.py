from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Method 1
# driver.save_screenshot("C://Users//Prerna Singh//Desktop//Files//screenshots//homepage.png")
# Method 2
driver.save_screenshot(os.getcwd()+"//homepage.png")
# Method 3
# driver.get_screenshot_as_file(os.getcwd()+"//homepage.png")

# Method 4 # saves in binary format
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_base64()

driver.quit()

