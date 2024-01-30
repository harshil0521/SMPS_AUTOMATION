import time

from selenium.webdriver.common.by import By


def fnTruckArrival(driver):

    transaction = driver.find_element(By.XPATH, "//*[contains(text(), 'Transaction')]")
    transaction.click()

    bmcCollection = driver.find_element(By.XPATH, "//*[contains(text(), 'BMC Collection')]")
    bmcCollection.click()

    truckArrival = driver.find_element(By.XPATH, "//a[normalize-space()='Truck Arrival']")
    truckArrival.click()

    routeDrp = driver.find_element(By.NAME, "route")
    routeDrp.click()

    routes = driver.find_elements(By.XPATH, "/html/body/div/div/div/div//mat-option")
    print(len(routes))

    # for i in range(len(routes)):
    #     print("Route [", i+1, "] = ", routes[i].text)

    for i in range(len(routes)):
        route_selection = driver.find_element(By.XPATH, "//*[contains(text(), '"+routes[i].text+"')]")
        route_selection.click()

        submit = driver.find_element(By.XPATH, "//*[contains(text(), ' Submit ')]")
        submit.click()

        route_dropdown = driver.find_element(By.NAME, "route")
        route_dropdown.click()
        time.sleep(0.5)

