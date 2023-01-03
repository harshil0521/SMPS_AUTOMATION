from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.foundit.in/")
driver.find_element(By.XPATH, "//div[@class='heroSection-buttonContainer_secondaryBtn secondaryBtn']").click()
resume = driver.find_element(By.XPATH, "//input[@id='file-upload']")
resume.send_keys("C:/Users/Prerna Singh/Desktop/Files/Lines.txt")
