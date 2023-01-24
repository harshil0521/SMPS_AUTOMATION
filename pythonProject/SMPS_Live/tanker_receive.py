from selenium import webdriver
from selenium.webdriver.common.by import By
from log_in_screen import fn_log_in
import time


driver = webdriver.Chrome()
driver.get('http://localhost:4200/#/login')
driver.implicitly_wait(10)
driver.maximize_window()


fn_log_in(driver)

driver.find_element(By.XPATH, "//span[normalize-space()='Transaction']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Tanker BMC Movement']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Tanker Receive']").click()

rec_button = driver.find_elements(By.XPATH, "//mat-table[@role='table']/mat-row/mat-cell[14]/button[2]")
print(len(rec_button))

for i in range(len(rec_button)):
    if rec_button[i].is_enabled():
        driver.find_element(By.XPATH, "//mat-table[@role='table']/mat-row/mat-cell[14]/button["+str(i)+"]").click()

driver.close()
