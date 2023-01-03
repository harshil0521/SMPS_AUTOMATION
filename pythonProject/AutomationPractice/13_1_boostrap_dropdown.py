from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
countries = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print(len(countries))

for c in countries:
    if c.text == 'Brazil':
        c.click()
        break

# How to capture the screenshot of webpage


time.sleep(3)
driver.quit()
