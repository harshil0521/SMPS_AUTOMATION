from selenium import webdriver
from log_in import log_in
import time
from truck_arrival import truck_arrival
from dock_collection import dock_collection


driver = webdriver.Chrome()
driver.get('http://localhost:4200/#/login')
driver.implicitly_wait(10)
driver.maximize_window()


log_in(driver)


# truck_arrival(driver)
#dock_collection(driver)


time.sleep(5)
driver.quit()
