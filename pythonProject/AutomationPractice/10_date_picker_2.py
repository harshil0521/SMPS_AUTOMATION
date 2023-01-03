from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//input[@id='dob']").click()
m_drp = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
m_drp.select_by_visible_text("May")

y_drp = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
y_drp.select_by_visible_text("1999")

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text == "21":
        ele.click()
        break
