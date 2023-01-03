from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # renaming expected_conditions to EC
                                                                  # (EC is alias of expected_condition)
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

"----------------------------------------------------------------------"
""" Wait Commands"""
"----------------------------------------------------------------------"
# import time
# 1.performance of the script is poor
# 2. If the element is not available in mentioned time, then there is still chance of getting exception error.
# time.sleep(time in seconds)


"----------------------------------------------------------------------"
# 1. implicit wait
"----------------------------------------------------------------------"
# only single time calling the wait function

# driver.implicitly_wait(10)
# driver.maximize_window()
# search = driver.find_element(By.XPATH, "//input[@title='Search']")
# search.send_keys('Selenium')
# search.submit()
# driver.find_element(By.XPATH, "//h3[text()='Selenium Tutorial - Guru99']").click()

"----------------------------------------------------------------------"
# 2. Explicit wait
"----------------------------------------------------------------------"

# Explicit wait works based on condition.
# Works more effectively

"""explicit wait declaration"""
# my_wait = WebDriverWait(driver, 10)  time is cutout to wait for the element # basic syntax
my_wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[RuntimeWarning, FileNotFoundError, Exception])
"""Poll frequency, interval of time for which command will go and look for element"""

search_link = my_wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium Tutorial - Guru99']")))
search_link.click()

driver.quit()

