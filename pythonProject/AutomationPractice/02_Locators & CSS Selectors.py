from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.nopcommerce.com/en")

# """For single element"""
# driver.find_element(By.ID, "Value of ID")
# driver.find_element(By.NAME, "Value of NAME" )
# driver.find_element(By.LINK_TEXT, "Value of LINK_TEXT")
# driver.find_element(By.PARTIAL_LINK_TEXT, "Value of PARTIAL_LINK_TEXT")

# """For multiple elements"""
# driver.find_elements(By.CLASS_NAME, "Value of CLASS_NAME")
# driver.find_elements(By.TAG_NAME, "Value of TAG_NAME")


# """CSS Selectors (Cascading Style Sheets )"""

# "1. Tag & ID"
# driver.find_element(By.CSS_SELECTOR, "tag name#valueofID")
# driver.find_element(By.CSS_SELECTOR, "#valueofID")

# "2. Tag & CLASS"
# driver.find_element(By.CSS_SELECTOR, "tag name.value of CLASS")
# driver.find_element(By.CSS_SELECTOR, ".value of CLASS")

# "3. Tag & Attribute"
# driver.find_element(By.CSS_SELECTOR, "tag name[attribute=value of attribute]")
# driver.find_element(By.CSS_SELECTOR, "[attribute=value of attribute]")

# "4. Tag, CLASS & Attribute"
# driver.find_element(By.CSS_SELECTOR, "tag name.value of CLASS[attribute=value of attribute]")


""" Difference between find_element and find_elements """

""" driver.find_element()   # always return single web element"""

# 1. Locator matching with single element
# element = driver.find_element(By.XPATH, "Location of single web element")
# element.send_keys("")

# 2. Locator matching with multiple element
# element = driver.find_element(By.XPATH, "Location of Multiple web element")
# print(element.text)

# 3. Element is not available
# element = driver.find_element(By.XPATH, "Location of unavailable web element") # This will return NoSuchElementException


""" driver.find_elements()   # always return list of web element"""

# 1. Locator matching with single element
# elements = driver.find_elements(By.XPATH, "Location of single web element")   # It always returns list collection
# print(len(elements))    # We can't use send keys method
# print(elements[0].send_keys(''))


# 2. Locator matching with multiple element
# elements = driver.find_elements(By.XPATH, "Location of Multiple web element")
# print(len(elements))    # total number of elements
# print(elements[0].text)    # printing first element
# for ele in elements:    # printing all elements
# print(ele.text)


# 3. Element is not available
# elements = driver.find_elements(By.XPATH, "Location of unavailable web element") # This will return NoSuchElementException
# print(len(elements))    # total number of elements, it will not throw exception, it will return 0.

# Difference
# 1. find_element return single element, find_elements return list.
# 2. find_element return NoSuchElementException if element is not found, find_elements will return 0.

""" text vs get_attribute('value') """

# driver.get("https://admin-demo.nopcommerce.com/login")

# text will always return inner text of the element
# get_attribute('any attribute') will return values of any web element
