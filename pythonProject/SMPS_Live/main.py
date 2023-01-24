from selenium import webdriver
from log_in_screen import fn_log_in
import time
from truck_arrival_screen import fn_truck_arrival
from dock_collection_screen import dock_collection

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('http://proc.smartmps.in/#/login')

fn_log_in(driver)
fn_truck_arrival(driver)
# dock_collection(driver)

time.sleep(5)
driver.quit()
