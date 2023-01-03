from selenium import webdriver
from selenium.webdriver.common.by import By
from dock_collection import dock_collection
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Prerna Singh\Downloads\chromedriver_win32\chromedriver.exe")
driver.get('http://dev.rmrd.in/#/login')
# time.sleep(1)
driver.implicitly_wait(3)
element = driver.find_element(By.NAME, "phone_number")
element.clear()
element.send_keys("9925044205")
element = driver.find_element(By.NAME, "password")
element.clear()
element.send_keys("admin123456")
driver.find_element(By.ID, "login-form-wrapper").click()  # login button
driver.find_element(By.ID, "mat-select-value-1").click()  # dock dropdown
driver.find_element(By.ID, "mat-option-2").click()        # dock selection
driver.find_element(By.ID, "mat-select-value-3").click()  # shift
driver.find_element(By.ID, "mat-option-0").click()  # shift selection
driver.find_element(By.XPATH, "//*[@id='mat-dialog-0']/app-is-collection/mat-card/mat-dialog-actions/div[2]/button").click()  # continue
driver.implicitly_wait(5)
driver.find_ele



