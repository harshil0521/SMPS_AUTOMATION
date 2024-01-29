from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def fnLabCollection(driver):
    driver.implicitly_wait(10)
    # transaction = driver.find_element(By.XPATH, "//*[contains(text(), 'Transaction')]")
    # transaction.click()
    #
    # bmcCollection = driver.find_element(By.XPATH, "//*[contains(text(), 'BMC Collection')]")
    # bmcCollection.click()

    labCollection = driver.find_element(By.XPATH, "//*[contains(text(), 'Lab Collection')]")
    labCollection.click()

    trayNo = driver.find_element(By.NAME, "tray")
    # trayNo.click()
    trayNo.send_keys('1')

    fetchbtn = driver.find_element(By.XPATH, "//*[contains(text(), 'Fetch')]")
    fetchbtn.click()

    fatValue = driver.find_element(By.XPATH, "(//mat-cell[@role='cell'])[7]")
    time.sleep(5)
    fatValue.clear()
    fatValue.send_keys('5')

    snfValue = driver.find_element(By.ID, "mat-input-18")
    snfValue.click()
    snfValue.send_keys('10')
