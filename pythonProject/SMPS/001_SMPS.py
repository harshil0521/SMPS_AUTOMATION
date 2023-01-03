import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"C:\Users\Prerna Singh\Downloads\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get('http://dev.rmrd.in/#/login')
driver.implicitly_wait(5)

#Login

driver.find_element(By.ID, "mat-input-0").send_keys("9292929292")
driver.find_element(By.ID, "mat-input-1").send_keys("admin123456")
driver.find_element(By.XPATH, "//*[@id='login-form-wrapper']/div/form/div/button").click()

#member collection

driver.find_element(By.XPATH, "//*[@id='snav']/div/app-sidebar/mat-nav-list/mat-list-item[3]/span/a").click()
driver.find_element(By.XPATH, "//*[@id='mat-menu-panel-5']/div/button[2]").click()
driver.find_element(By.XPATH, "//*[@id='mat-menu-panel-9']/div/button[1]").click()
driver.find_element(By.XPATH, "//*[@id='mat-select-value-7']/span").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='mat-select-value-9']/span").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/app-root/app-full-layout/div/mat-sidenav-container/mat-sidenav-content/div/app-farmer-collection-manual/div/div[2]/div/div/form/div[1]/div[6]/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='mat-select-value-11']/span").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/app-root/app-full-layout/div/mat-sidenav-container/mat-sidenav-content/div/app-farmer-collection-manual/div/div[2]/div/div/form/div[1]/div[8]/button[1]").click()

#driver.close()