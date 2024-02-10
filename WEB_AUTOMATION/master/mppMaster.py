from selenium.webdriver.common.by import By
from WEB_AUTOMATION import XLUtility
import time

def fnMPPMaster (driver):
    driver.find_element(By.XPATH, "//*[contains(text(), 'Master')]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Collection Points')]").click()
    driver.find_element(By.XPATH, "//*[@href='#/master/society']").click()

    file = "C:/Samudra Project/AUTOMATION/SMPS_AUTOMATION/WEB_AUTOMATION/dataSheet/mppMaster.xlsx"
    rows = XLUtility.getRowCount(file, "data")
    # print(rows)

    for r in range(2, rows+1):
        """Reading Data"""
        mppCode = XLUtility.readData(file, "data", r, 1)
        mppName = XLUtility.readData(file, "data", r, 2)
        sapMPPCode = XLUtility.readData(file, "data", r, 3)
        sapRouteCode = XLUtility.readData(file, "data", r, 4)
        sapPlantCode = XLUtility.readData(file, "data", r, 5)
        mobile = XLUtility.readData(file, "data", r, 6)
        bmc = XLUtility.readData(file, "data", r, 7)
        route = XLUtility.readData(file, "data", r, 8)
        country = XLUtility.readData(file, "data", r, 9)
        state = XLUtility.readData(file, "data", r, 10)
        district = XLUtility.readData(file, "data", r, 11)
        subDistrict = XLUtility.readData(file, "data", r, 12)
        village = XLUtility.readData(file, "data", r, 13)
        effectiveDate = XLUtility.readData(file, "data", r, 14)
        effectiveShift = XLUtility.readData(file, "data", r, 15)

        """Passing Data"""
        driver.find_element(By.XPATH, "//*[contains(text(), 'add_circle')]").click()

        driver.find_element(By.XPATH, "//*[@data-placeholder='MPP Code']").click()
        driver.find_element(By.XPATH, "//*[contains(text(), '"+mppCode+"')]").click()

        driver.find_element(By.XPATH, "//*[@data-placeholder='MPP Name']").click()
        driver.find_element(By.XPATH, "//*[contains(text(), '"+mppName+"')]").click()

        driver.find_element(By.XPATH, "//*[@data-placeholder='Sap MPP Code']").click()
        driver.find_element(By.XPATH, "//*[contains(text(), '"+sapMPPCode+"')]").click()

        driver.find_element(By.XPATH, "//*[@placeholder='Route']").click()
        driver.find_element(By.XPATH, "//*[contains(text(), '"+route+"')]").click()

        driver.find_element(By.XPATH, "//*[@placeholder='MPP']").click()
        driver.find_element(By.XPATH, "//*[contains(text(), '"+mpp+"')]").click()
        # driver.find_element(By.XPATH, "//*[@placeholder='MPP']").send_keys(mpp)

        driver.find_element(By.XPATH, "//*[@data-placeholder='First Name']").send_keys(firstName)
        driver.find_element(By.XPATH, "//*[@data-placeholder='Last Name']").send_keys(lastName)
        driver.find_element(By.XPATH, "//*[@data-placeholder='Member Code']").send_keys(memberCode)
        driver.find_element(By.XPATH, "//*[@data-placeholder='Other Code']").send_keys(otherCode)
        driver.find_element(By.XPATH, "//*[@placeholder='Gender']").send_keys(gender)
        driver.find_element(By.XPATH, "//*[@data-placeholder='Address Line1']").send_keys(addressLine)
        driver.find_element(By.XPATH, "//*[@placeholder=' Country']").send_keys(country)
        driver.find_element(By.XPATH, "//*[@placeholder=' State']").send_keys(state)
        driver.find_element(By.XPATH, "//*[@placeholder=' District']").send_keys(district)
        driver.find_element(By.XPATH, "//*[@placeholder=' Subdistrict']").send_keys(subDistrict)
        driver.find_element(By.XPATH, "//*[@placeholder=' Village']").send_keys(village)
        driver.find_element(By.XPATH, "//*[@data-placeholder='Mobile']").send_keys(mobileNo)
        driver.find_element(By.XPATH, "//*[@data-placeholder='Effective Date']").send_keys(effectiveDate)
        driver.find_element(By.XPATH, "//*[@data-placeholder='Approval Date']").send_keys(approvalDate)
        driver.find_element(By.XPATH, "//*[@formcontrolname='isActive']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Add']").click()
        time.sleep(1)
    print("Total", rows-1, "Member Added.")
    time.sleep(2)
    driver.close()
