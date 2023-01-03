from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://dev.rmrd.in/#/login")
driver.maximize_window()
driver.implicitly_wait(5)

"""Number & Password"""
phone_number = driver.find_element(By.NAME, "phone_number")
# phone_number.clear()
phone_number.send_keys("9925044205")
password = driver.find_element(By.NAME, "password")
# password.clear()
password.send_keys("admin123456")
password.send_keys(Keys.RETURN)

"""Dock & Shift selection"""
dock_dropdown = driver.find_element(By.NAME, "dock")
dock_dropdown.click()
dock_selection = driver.find_element(By.ID, "mat-option-2")
dock_selection.click()
shift = driver.find_element(By.NAME, "shift")
shift.click()
selected_shift = driver.find_element(By.XPATH, "//*[contains(text(), 'Morning')]")
#   selected_shift = driver.find_element(By.XPATH, "//*[contains(text(), 'Evening')]")
selected_shift.click()
submit = driver.find_element(By.XPATH, "//*[contains(text(), 'Submit')]")
submit.click()
time.sleep(0.5)

driver.find_element(By.XPATH, "//mat-list-item[2]//span[1]//a[1]").click()
driver.find_element(By.XPATH, "//button[contains(text(),'MPP')]").click()

# finding total rows in a table
rows = len(driver.find_elements(By.XPATH, "//mat-table[@role='table']//mat-row"))
print("Total number of rows is :", rows)
count = 0
for r in range(1, rows+1):
    activity = driver.find_element(By.XPATH, " //mat-table[@role='table']//mat-row["+str(r)+"]/mat-cell[6]").text
    if activity == "Yes":
        count += 1
    print(activity)
print(count)
time.sleep(2)
driver.close()
