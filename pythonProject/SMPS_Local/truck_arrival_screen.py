from selenium.webdriver.common.by import By


def fn_truck_arrival(driver):

    transaction = driver.find_element(By.XPATH, "//*[contains(text(), 'Transaction')]")
    transaction.click()

    auto_collection = driver.find_element(By.XPATH, "//*[contains(text(), 'Auto Collection')]")
    auto_collection.click()

    truck = driver.find_element(By.XPATH, "//button[normalize-space()='Truck Arrival']")
    truck.click()

    route_drp = driver.find_element(By.NAME, "route")
    route_drp.click()

    routes = driver.find_elements(By.XPATH, "/html/body/div/div/div/div//mat-option")
    print(len(routes))

    for i in range(len(routes)):
        print("Route [", i+1, "] = ", routes[i].text)

    for i in range(len(routes)):
        route_selection = driver.find_element(By.XPATH, "//*[contains(text(), '"+routes[i].text+"')]")
        route_selection.click()

        submit = driver.find_element(By.XPATH, "//*[contains(text(), ' Submit ')]")
        submit.click()

        route_dropdown = driver.find_element(By.NAME, "route")
        route_dropdown.click()
