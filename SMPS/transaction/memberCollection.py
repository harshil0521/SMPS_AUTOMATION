from selenium.webdriver.common.by import By
import XLUtility
import time


def fnMemberCollection(driver):

    transaction = driver.find_element(By.XPATH, "//*[contains(text(), 'Transaction')]")
    transaction.click()

    mppCollection = driver.find_element(By.XPATH, "//*[contains(text(), 'MPP Collection')]")
    mppCollection.click()

    memberCollection  = driver.find_element(By.XPATH, "//*[contains(text(), 'Member Collection')]")
    memberCollection.click()

    file = "C:/Samudra Project/AUTOMATION/SMPS_AUTOMATION/SMPS/dataSheet/memberCollectionData.xlsx"
    rows = XLUtility.getRowCount(file, "data")

    for r in range(2, rows+1):

        driver.refresh()
        """Reading data"""
        routeValue = XLUtility.readData(file, "data", r, 1)
        mppValue = XLUtility.readData(file, "data", r, 2)
        dateValue = XLUtility.readData(file, "data", r, 3)
        print(dateValue) #01-06-2023
        newDateValue = dateValue.split('-')
        dateValue2 = newDateValue[0]
        monthValue = newDateValue[1]
        yearValue = newDateValue[2]
        shiftValue = XLUtility.readData(file, "data", r, 4)
        memberValue = XLUtility.readData(file, "data", r, 5)
        typeValue = XLUtility.readData(file, "data", r, 6)
        quantityValue = XLUtility.readData(file, "data", r, 7)
        fatValue = XLUtility.readData(file, "data", r, 8)
        snfValue = XLUtility.readData(file, "data", r, 9)

        routeDropdown = driver.find_element(By.NAME, "Route")
        routeDropdown.click()

        route = driver.find_element(By.XPATH, "//*[contains(text(), '"+routeValue+"')]")
        route.click()
        # time.sleep(5)

        mppDropdown = driver.find_element(By.NAME, "Society")  
        mppDropdown.click()

        mpp = driver.find_element(By.XPATH, "//*[contains(text(), '"+mppValue+"')]")
        mpp.click()

        date = driver.find_element(By.XPATH, "//button[@aria-label='Open calendar']")
        date.click()

        # datePicker = driver.find_element(By.XPATH, "//button[@aria-label='21 July 2023']")
        # datePicker.click()


        datePicker = driver.find_element(By.XPATH, "//button[@aria-label='Choose month and year']")
        datePicker.click()

        yearSelection = driver.find_element(By.XPATH, "//*[contains(text(), '"+yearValue+"')]")
        yearSelection.click()

        monthSelection = driver.find_element(By.XPATH, "//*[contains(text(), '"+monthValue+"')]")
        monthSelection.click()
        time.sleep(1)
        
        print("Date:", dateValue2)
        dateSelect = driver.find_element(By.XPATH, "//*[contains(text(), ' "+dateValue2+" ')]")
        dateSelect.click()
        # dateSelection = driver.find_element(By.XPATH, "//*[contains(text(), '21')]")
        # dateSelection.click()
        print(dateValue2)

        # dateSelection = driver.find_element(By.XPATH, "//button[@aria-label='"+dateValue+"']")
        # dateSelection.click()

        shift = driver.find_element(By.NAME, "shift")
        shift.click()

        # shiftSelection = driver.find_element(By.XPATH, "//*[contains(text(), '"+shiftValue+"')]")
        shiftSelection = driver.find_element(By.XPATH, "//span[@class='mat-option-text'][normalize-space()='"+shiftValue+"']")
        shiftSelection.click() 

        # fetch = driver.find_element(By.XPATH, "//i[normalize-space()='search']")
        # fetch.click()

        add = driver.find_element(By.XPATH, "//i[normalize-space()='add']")
        add.click()

        """Collection screen"""

        member = driver.find_element(By.XPATH, "//*[contains(text(), '"+memberValue+"')]")
        member.click()

        typeDropdown = driver.find_element(By.ID, "type")
        typeDropdown.click()

        milkType = driver.find_element(By.XPATH, "//span[normalize-space()='"+typeValue+"']")
        milkType.click()

        quantity = driver.find_element(By.NAME, "qty")
        quantity.clear()
        quantity.send_keys(quantityValue)

        fat = driver.find_element(By.NAME, "fat")
        fat.clear()
        fat.send_keys(fatValue)

        snf = driver.find_element(By.NAME, "snf")
        snf.clear()
        snf.send_keys(snfValue)

        add = driver.find_element(By.ID, "buttonAdd")
        add.click()

        close = driver.find_element(By.XPATH, "//mat-icon[normalize-space()='close']")
        close.click() 