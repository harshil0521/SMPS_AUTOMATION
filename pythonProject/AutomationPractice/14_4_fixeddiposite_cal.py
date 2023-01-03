import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from AutomationPractice import data_driven_test_utility_14_3_

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()
driver.find_element(By.ID, "wzrk-cancel").click()

file = "C:/Users/Prerna Singh/Desktop/Files/bugsheettest.xlsx"
rows = data_driven_test_utility_14_3_.getRowCount(file, "Sheet2")
for r in range(2, rows+1):
    # reading data
    principle = data_driven_test_utility_14_3_.readData(file, "Sheet2", r, 1)
    rot = data_driven_test_utility_14_3_.readData(file, "Sheet2", r, 2)
    period1 = data_driven_test_utility_14_3_.readData(file, "Sheet2", r, 3)
    period2 = data_driven_test_utility_14_3_.readData(file, "Sheet2", r, 4)
    freq = data_driven_test_utility_14_3_.readData(file, "Sheet2", r, 5)
    maturity = data_driven_test_utility_14_3_.readData(file, "Sheet2", r, 6)

    # passing data to the application
    driver.find_element(By.NAME, "principal").send_keys(principle)
    driver.find_element(By.NAME, "interest").send_keys(rot)
    driver.find_element(By.NAME, "tenure").send_keys(period1)
    perioddrp = Select(driver.find_element(By.NAME, "tenurePeriod"))
    perioddrp.select_by_visible_text(period2)
    freqdrp = Select(driver.find_element(By.NAME, "frequency"))
    freqdrp.select_by_visible_text(freq)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    act_maturity = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    # validation
    if float(maturity) == float(act_maturity):
        print("Test Passed")
        data_driven_test_utility_14_3_.writeData(file, "Sheet2", r, 8, "Passed")
        data_driven_test_utility_14_3_.fillGreenColor(file, "Sheet2", r, 8)
    else:
        print("Test Failed")
        data_driven_test_utility_14_3_.writeData(file, "Sheet2", r, 8, "Failed")
        data_driven_test_utility_14_3_.fillRedColor(file, "Sheet2", r, 8)

    # clearing form
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(0.5)

driver.close()
