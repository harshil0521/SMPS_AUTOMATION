from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Prerna Singh\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf5LF0BSGp7DAhVP8GmlilNicISW7g4S3l9GAFeSIzqPhW0Yg/viewform?usp=sf_link")

select = Select(driver.find_element_by_class_name("MocG8c HZ3kWc mhLiyf OIC90c LMgvRb"))
# select.select_by_value("AMERICAN SAMOA")