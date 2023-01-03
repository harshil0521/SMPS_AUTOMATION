from selenium import webdriver
from log_in import log_in
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from truck_arrival import truck_arrival
from dock_collection import dock_collection


driver = webdriver.Chrome(executable_path=r"C:\Users\Prerna Singh\Downloads\chromedriver_win32\chromedriver.exe")
driver.get('http://dev.rmrd.in/#/login')
driver.implicitly_wait(2)

log_in(driver)
