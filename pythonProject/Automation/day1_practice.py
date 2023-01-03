from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

# serv_obj = Service("D:\\PycharmProjects\\chromedriver_win32\\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

search = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
search.send_keys("Selenium")
search.send_keys(Keys.RETURN)

