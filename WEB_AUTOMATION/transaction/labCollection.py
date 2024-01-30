from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def fnLabCollection(driver):
    driver.implicitly_wait(10)
    transaction = driver.find_element(By.XPATH, "//*[contains(text(), 'Transaction')]")
    transaction.click()

    bmcCollection = driver.find_element(By.XPATH, "//*[contains(text(), 'BMC Collection')]")
    bmcCollection.click()

    labCollection = driver.find_element(By.XPATH, "//*[contains(text(), 'Lab Collection')]")
    labCollection.click()

    trayNo = driver.find_element(By.NAME, "tray")
    # trayNo.click()
    trayNo.send_keys('1')

    fetchButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Fetch')]")
    fetchButton.click()

    fatValue = driver.find_element(By.XPATH, "//mat-table[@role='table']/mat-row[1]/mat-cell[7]//input")
    fatValue.clear()
    fatValue.send_keys('5')

    snfValue = driver.find_element(By.XPATH, "//mat-table[@role='table']/mat-row[1]/mat-cell[8]//input")
    snfValue.clear()
    snfValue.send_keys('10')

    update = driver.find_element(By.XPATH, "//mat-icon[normalize-space()='check']")
    update.click()
