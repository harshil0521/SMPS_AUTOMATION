import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from WEB_AUTOMATION import XLUtility


def fnMemberMaster(driver):

    driver.find_element(By.XPATH, "//*[contains(text(), 'Master')]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Collection Points')]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Member')]").click()

    file = "C:/Samudra Project/AUTOMATION/SMPS_AUTOMATION/WEB_AUTOMATION/dataSheet/memberMaster.xlsx"
    rows = XLUtility.getRowCount(file, "data")
    # print(rows)

    for r in range(2, rows+1):
        """Reading Data"""
        plant = XLUtility.readData(file, "data", r, 1)
        mcc = XLUtility.readData(file, "data", r, 2)
        bmc = XLUtility.readData(file, "data", r, 3)
        route = XLUtility.readData(file, "data", r, 4)
        mpp = XLUtility.readData(file, "data", r, 5)
        firstName = XLUtility.readData(file, "data", r, 6)
        lastName = XLUtility.readData(file, "data", r, 7)
        memberCode = XLUtility.readData(file, "data", r, 8)
        # otherCode = XLUtility.readData(file, "data", r, 8)
        otherCode = memberCode
        gender = XLUtility.readData(file, "data", r, 9)
        addressLine = XLUtility.readData(file, "data", r, 10)
        country = XLUtility.readData(file, "data", r, 11)
        state = XLUtility.readData(file, "data", r, 12)
        district = XLUtility.readData(file, "data", r, 13)
        subDistrict = XLUtility.readData(file, "data", r, 14)
        village = XLUtility.readData(file, "data", r, 15)
        mobileNo = XLUtility.readData(file, "data", r, 16)
        effectiveDate = str(XLUtility.readData(file, "data", r, 17))
        # approvalDate = XLUtility.readData(file, "data", r, 17)
        approvalDate = effectiveDate

        """Passing Data"""
        driver.find_element(By.XPATH, "//*[contains(text(), 'add_circle')]").click()

        driver.find_element(By.XPATH, "//*[@placeholder='Plant ']").click()
        driver.find_element(By.XPATH, "//*[contains(text(), '"+plant+"')]").click()

        driver.find_element(By.XPATH, "//*[@placeholder='MCC']").click()
        driver.find_element(By.XPATH, "//*[contains(text(), '"+mcc+"')]").click()

        driver.find_element(By.XPATH, "//*[@placeholder='BMC']").click()
        driver.find_element(By.XPATH, "//*[contains(text(), '"+bmc+"')]").click()

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
