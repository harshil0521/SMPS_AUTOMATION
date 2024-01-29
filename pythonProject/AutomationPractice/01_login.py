from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
import time

# serv_obj = Service("C:\Users\Prerna Singh\Downloads\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service = serv_obj)
driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(1)
driver.find_element(By.NAME, "username").send_keys('Admin')
driver.find_element(By.NAME, "password").send_keys('admin123')
driver.find_element(By.ID, "app").click()
act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login test passed")
else:
    print("Login test failed")

driver.close()