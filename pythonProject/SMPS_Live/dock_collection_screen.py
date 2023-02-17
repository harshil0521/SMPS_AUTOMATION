from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def fn_dock_collection(driver):
    transaction = driver.find_element(By.XPATH, "//*[contains(text(), 'Transaction')]")
    transaction.click()

    auto_collection = driver.find_element(By.XPATH, "//*[contains(text(), 'Auto Collection')]")
    auto_collection.click()

    dock = driver.find_element(By.XPATH, "//*[contains(text(), 'Dock')]")
    dock.click()

    route_dropdown = driver.find_element(By.NAME, "routeSelect")
    route_dropdown.click()

    routes = driver.find_elements(By.XPATH, "/html/body/div[3]/div[4]//mat-option")
    print(len(routes))

    route = routes[1]
    route_select = driver.find_element(By.XPATH, "//*[contains(text(), '"+route+"')]")
    route_select.click()

    grade_dropdown = driver.find_element(By.NAME, "grade")
    grade_dropdown.click()

    grade = driver.find_element(By.XPATH, "//*[contains(text(), 'Good')]")
#   grade = driver.find_element(By.XPATH, "//*[contains(text(), 'Sour')]")
#   grade = driver.find_element(By.XPATH, "//*[contains(text(), 'Curd')]")
    grade.click()

    continues = driver.find_element(By.XPATH, "//*[contains(text(), ' Continue ')]")
    continues.click()


    codes = ['1010', '12125']

    for code in codes:
        time.sleep(0.25)
        mpp_code = driver.find_element(By.NAME, "Code")
        mpp_code.clear()
        mpp_code.send_keys(code)

    #    milk_dropdown = driver.find_element(By.ID, "mat-input-15")
    #    milk_dropdown.click()

    #   milk_type = driver.find_element(By.ID, "mat-option-71")
    #   milk_type = driver.find_element(By.XPATH, "//*[contains(text(), 'B')]")
    #   milk_type.click()

        rec_can = driver.find_element(By.NAME, "Rec_Can")
        rec_can.clear()
        rec_can.send_keys('1')

        quantity = driver.find_element(By.NAME, "Weight")
        quantity.clear()
        quantity.send_keys('15')

        add_qty = driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]")
        add_qty.click()

        try:
            duplicate = driver.find_element(By.XPATH, "//*[contains(text(), 'Yes')]")
            duplicate.click()
        except NoSuchElementException:
            print("First time collection of party code", code)








