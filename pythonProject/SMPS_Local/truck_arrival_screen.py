from selenium.webdriver.common.by import By


def fn_truck_arrival(driver):
    transaction = driver.find_element(By.XPATH, "//*[contains(text(), 'Transaction')]")
    transaction.click()

    auto_collection = driver.find_element(By.XPATH, "//*[contains(text(), 'Auto Collection')]")
    auto_collection.click()

    truck = driver.find_element(By.XPATH, "//*[@id='mat-menu-panel-10']/div/button[1]")
    truck.click()

    route_dropdown = driver.find_element(By.ID, "mat-select-value-5")
    route_dropdown.click()

    route_selection = driver.find_element(By.XPATH, "//*[contains(text(), ' [006] DEMO ROUTE ')]")
    route_selection.click()

    submit = driver.find_element(By.XPATH, "//*[contains(text(), ' Submit ')]")
    submit.click()
