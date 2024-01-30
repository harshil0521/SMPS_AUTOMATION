from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from WEB_AUTOMATION import XLUtility
import time

def fnTankerReceive(driver):
    driver.find_element(By.XPATH, "//*[contains(text(), 'Transaction')]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'BMC Tanker Movement')]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Tanker Receive')]").click()

    file = "C:/Samudra Project/AUTOMATION/SMPS_AUTOMATION/WEB_AUTOMATION/dataSheet/tankerReceiveData.xlsx"
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
        seal_no = XLUtility.readData(file, "data", r, 8)
        rawNo = str(r-1)
        """passing data to the application"""
        driver.find_element(By.XPATH, "//mat-row["+rawNo+"]//mat-cell[14]/child::button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='qty' and @aria-required='true']").send_keys(quantity)
        driver.find_element(By.XPATH, "//input[@name='fat' and @aria-required='true']").send_keys(fat)
        driver.find_element(By.XPATH, "//input[@name='snf' and @aria-required='true']").send_keys(snf)
        driver.find_element(By.XPATH, "//input[@name='lr' and @aria-required='true']").send_keys(lr)
        driver.find_element(By.XPATH, "//input[@name='temperature' and @aria-required='true']").send_keys(temp)
        driver.find_element(By.XPATH, "//input[@name='acidity' and @aria-required='true']").send_keys(acidity)
        driver.find_element(By.XPATH, "//mat-select[@name='cob' and @aria-required='true']").click()
        if cob == "Positive":
            driver.find_element(By.XPATH, "//*[contains(text(),'Positive')]").click()
        else:
            driver.find_element(By.XPATH, "//*[contains(text(), 'Negative')]").click()
        driver.find_element(By.XPATH, "//input[@name='sealNo' and @aria-required='true']").send_keys(seal_no)
        driver.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
        time.sleep(1)
