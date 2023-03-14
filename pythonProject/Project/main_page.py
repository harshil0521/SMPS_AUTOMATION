import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service

serv_obj = Service("D:/drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome()
# driver = webdriver.Chrome(executable_path=r"D:\drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.youtube.com/")
