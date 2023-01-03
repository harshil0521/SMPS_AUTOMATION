from selenium import webdriver
from selenium.webdriver.common.by import By
from log_in import log_in
import time


driver = webdriver.Chrome()
driver.get('http://localhost:4200/#/login')
driver.implicitly_wait(10)
driver.maximize_window()


log_in(driver)

driver.find_element(By.XPATH, "//span[normalize-space()='Transaction']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Tanker BMC Movement']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Tanker Dispatch']").click()

# Adding new record
quantity = float(150)
fat = float(5)
snf = float(10)
lr = float(16)
temperature = float(38)
acidity = int(4)


for i in range(2):
    driver.find_element(By.XPATH, "//mat-icon[normalize-space()='add_circle']").click()
    driver.find_element(By.NAME, "qty").send_keys(quantity)
    driver.find_element(By.NAME, "fat").send_keys(fat)
    driver.find_element(By.NAME, "snf").send_keys(snf)
    driver.find_element(By.NAME, "lr").send_keys(lr)
    driver.find_element(By.NAME, "temperature").send_keys(temperature)
    driver.find_element(By.NAME, "acidity").send_keys(acidity)
    driver.find_element(By.NAME, "cob").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='Positive']").click()
    driver.find_element(By.NAME, "vehicleNo").send_keys("GJ123")
    driver.find_element(By.NAME, "sealNo").send_keys("123")
    driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator btn btn-primary m-2 float-right mat-raised-button mat-button-base ng-star-inserted']").click()
    quantity = quantity + 2.5
    fat = fat + 0.1
    snf = snf + 0.1
    lr = lr + 0.1
    temperature = temperature + 2
    acidity = acidity + 1
    time.sleep(0.5)








