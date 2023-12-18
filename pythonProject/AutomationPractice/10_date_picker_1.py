from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.implicitly_wait(10)

screen = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
driver.switch_to.frame(0)
# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("12/31/2022")

year = "2023"
month = "December"
date = "31"

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

# select month and year

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

#  select date

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
    if ele.text == date:
        ele.click()
        break 


# time.sleep(2)
# driver.quit()