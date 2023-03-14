from selenium import webdriver
from selenium.webdriver.common.service import Service

# serv_obj = Service("D:/drivers/chromedriver_win32/chromedriver.exe")
# driver = webdriver.Chrome()

serv_obj = Service("D:/drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.youtube.com/")
