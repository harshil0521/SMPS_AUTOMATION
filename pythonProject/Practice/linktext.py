from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Prerna Singh\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://dev.rmrd.in/#/login")
driver.implicitly_wait(3)
element = driver.find_element(By.NAME, "phone_number")
element.send_keys("9925044205")
element = driver.find_element(By.NAME, "password")
element.clear()
element.send_keys("admin123456")
element.send_keys(Keys.RETURN)
# driver.find_element(By.CLASS_NAME, "text-white mt-3 mb-3 btn submit-button ng-tns-c105-0").click()
dock_element = driver.find_element(By.XPATH, "//*[@id='mat-select-value-1']/span")
dock_element.click()
driver.find_element(By.ID, "mat-option-2").click()
dock_element.send_keys(Keys.SHIFT)


time.sleep(5)
driver.quit()

