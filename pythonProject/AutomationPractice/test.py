import logging
from selenium import webdriver

logging.getLogger('selenium').setLevel(logging.DEBUG)
driver = webdriver.Chrome()
driver.quit()