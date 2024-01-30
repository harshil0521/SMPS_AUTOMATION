from selenium.webdriver.common.by import By
from WEB_AUTOMATION import XLUtility
import time

def fnTankerDispatch(driver):
    driver.find_element(By.XPATH, "//*[contains(text(), 'Transaction')]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'BMC Tanker Movement')]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Tanker Dispatch')]").click()

    file = "C:/Samudra Project/AUTOMATION/SMPS_AUTOMATION/WEB_AUTOMATION/dataSheet/tankerDispatchData.xlsx"
    rows = XLUtility.getRowCount(file, "data")

    for r in range(2, rows+1):
        """reading data"""
        quantity = XLUtility.readData(file, "data", r, 1)
        fat = XLUtility.readData(file, "data", r, 2)
        snf = XLUtility.readData(file, "data", r, 3)
        lr = XLUtility.readData(file, "data", r, 4)
        temp = XLUtility.readData(file, "data", r, 5)
        acidity = XLUtility.readData(file, "data", r, 6)
        cob = XLUtility.readData(file, "data", r, 7)
        dri = XLUtility.readData(file, "data", r, 8)
        veh_no = XLUtility.readData(file, "data", r, 9)
        seal_no = XLUtility.readData(file, "data", r, 10)

        """passing data to the application"""
        driver.find_element(By.XPATH, "//mat-icon[normalize-space()='add_circle']").click()
        driver.find_elements(By.NAME, "qty").send_keys(quantity)
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
        driver.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
        time.sleep(1)
