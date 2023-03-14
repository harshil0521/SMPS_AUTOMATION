from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from log_in_screen import fn_log_in
from truck_arrival_screen import fn_truck_arrival
from dock_collection import dock_collection

serv_obj = Service("D:/drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.maximize_window()

# driver.get('http://dev.rmrd.in/#/login')
# driver.get('http://localhost:4200/#/login')
driver.get('http://proc.smartmps.in/#/login')

# fn_log_in(driver)
# fn_truck_arrival(driver)
# dock_collection(driver)

time.sleep(5)
driver.quit()
