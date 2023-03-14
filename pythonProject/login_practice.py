from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"D:\drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://phptravels.com/demo/")

firstname = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
firstname.send_keys('Harshil')
