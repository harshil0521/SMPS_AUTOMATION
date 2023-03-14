import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pythonProject.SMPS_Local import XLUtility
from selenium.webdriver.chrome.service import Service
from log_in_screen import fn_log_in

serv_obj = Service("D:/drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get('http://dev.rmrd.in/#/login')
driver.maximize_window()

fn_log_in(driver)

driver.find_element(By.XPATH, "//span[normalize-space()='Transaction']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Tanker BMC Movement']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Tanker Dispatch']").click()

file = "data/tanker_dispatch_data.xlsx"
rows = XLUtility.get_row_count(file, "data")

for r in range(2, rows+1):
    """reading data"""
    quantity = XLUtility.read_data(file, "data", r, 1)
    fat = XLUtility.read_data(file, "data", r, 2)
    snf = XLUtility.read_data(file, "data", r, 3)
    lr = XLUtility.read_data(file, "data", r, 4)
    temp = XLUtility.read_data(file, "data", r, 5)
    acidity = XLUtility.read_data(file, "data", r, 6)
    cob = XLUtility.read_data(file, "data", r, 7)
    dri = XLUtility.read_data(file, "data", r, 8)
    veh_no = XLUtility.read_data(file, "data", r, 9)
    seal_no = XLUtility.read_data(file, "data", r, 10)

    """passing data to the application"""
    driver.find_element(By.XPATH, "//mat-icon[normalize-space()='add_circle']").click()
    driver.find_element(By.NAME, "qty").send_keys(quantity)
    driver.find_element(By.NAME, "fat").send_keys(fat)
    driver.find_element(By.NAME, "snf").send_keys(snf)
    driver.find_element(By.NAME, "lr").send_keys(lr)
    driver.find_element(By.NAME, "temperature").send_keys(temp)
    driver.find_element(By.NAME, "acidity").send_keys(acidity)
    driver.find_element(By.NAME, "cob").click()
    if cob == "Positive":
        driver.find_element(By.XPATH, "//*[contains(text(),'Positive')]").click()
    else:
        driver.find_element(By.XPATH, "//*[contains(text(), 'Negative')]").click()
    driver.find_element(By.NAME, "driver").send_keys(dri)
    driver.find_element(By.NAME, "vehicleNo").send_keys(veh_no)
    driver.find_element(By.NAME, "sealNo").send_keys(seal_no)
    driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator btn btn-primary m-2 float-right mat-raised-button mat-button-base ng-star-inserted']").click()
    time.sleep(1)

driver.quit()
