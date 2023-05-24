from selenium.webdriver.common.by import By
from pythonProject.SMPS_Live import XLUtility
import time


def fn_member_collection(driver):
    transaction = driver.find_element(By.XPATH, "//*[contains(text(), 'Transaction')]")
    transaction.click()
    time.sleep(0.2)

    manual_entry = driver.find_element(By.XPATH, "//*[contains(text(), 'Manual Entry')]")
    manual_entry.click()
    # time.sleep(0.1)

    member_collection_data = driver.find_element(By.XPATH, "//*[contains(text(), 'Member Collection Data')]")
    member_collection_data.click()
    # time.sleep(0.5)

    file = "data/member_collection_data.xlsx"
    rows = XLUtility.get_row_count(file, "data")
    print(rows)
    time.sleep(2)

    for r in range(2, rows+1):

        driver.refresh()
        """Reading data"""
        route_value = XLUtility.read_data(file, "data", r, 1)
        mpp_value = XLUtility.read_data(file, "data", r, 2)
        date_value = XLUtility.read_data(file, "data", r, 3)
        # shift_value = XLUtility.read_data(file, "data", r, 4)
        member_value = XLUtility.read_data(file, "data", r, 5)
        type_value = XLUtility.read_data(file, "data", r, 6)
        quantity_value = XLUtility.read_data(file, "data", r, 7)
        fat_value = XLUtility.read_data(file, "data", r, 8)
        snf_value = XLUtility.read_data(file, "data", r, 9)

        route_dropdown = driver.find_element(By.NAME, "Route")
        route_dropdown.click()

        route = driver.find_element(By.XPATH, "//*[contains(text(), '"+route_value+"')]")
        route.click()
        # time.sleep(5)

        mpp_dropdown = driver.find_element(By.NAME, "Society")
        mpp_dropdown.click()

        mpp = driver.find_element(By.XPATH, "//*[contains(text(), '"+mpp_value+"')]")
        mpp.click()

        date = driver.find_element(By.XPATH, "//button[@aria-label='Open calendar']")
        date.click()

        date_selection = driver.find_element(By.XPATH, "//button[@aria-label='"+date_value+"']")
        date_selection.click()

        # shift = driver.find_element(By.NAME, "shift")
        # shift.click()
        # time.sleep(1)

        # shift_selection = driver.find_element(By.XPATH, "//*[contains(text(), '"+shift_value+"')]")
        # shift_selection.click()

        # fetch = driver.find_element(By.XPATH, "//i[normalize-space()='search']")
        # fetch.click()

        add = driver.find_element(By.XPATH, "//i[normalize-space()='add']")
        add.click()

        """Collection screen"""

        member = driver.find_element(By.XPATH, "//*[contains(text(), '"+member_value+"')]")
        member.click()

        type_dropdown = driver.find_element(By.ID, "type")
        type_dropdown.click()

        milk_type = driver.find_element(By.XPATH, "//span[normalize-space()='"+type_value+"']")
        milk_type.click()

        quantity = driver.find_element(By.NAME, "qty")
        quantity.clear()
        quantity.send_keys(quantity_value)

        fat = driver.find_element(By.NAME, "fat")
        fat.clear()
        fat.send_keys(fat_value)

        snf = driver.find_element(By.NAME, "snf")
        snf.clear()
        snf.send_keys(snf_value)

        add = driver.find_element(By.ID, "buttonAdd")
        add.click()
        time.sleep(1)

        close = driver.find_element(By.XPATH, "//mat-icon[normalize-space()='close']")
        close.click()
        time.sleep(1)
