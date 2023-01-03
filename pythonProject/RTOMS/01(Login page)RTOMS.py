from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Prerna Singh\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://www.rtoms.in/")
driver.implicitly_wait(5)
driver.maximize_window()

#Login
driver.find_element(By.ID, "phone_number").send_keys("1234567980")
driver.find_element(By.ID, "password").send_keys("123")
driver.find_element(By.XPATH, "/html/body/app-root/layout/empty-layout/div/div/auth-sign-in/div/div[1]/div/form/button").click()
time.sleep(3)
i = 1

#ProfileChange

driver.find_element(By.XPATH, "/html/body/app-root/layout/classy-layout/fuse-vertical-navigation/div/div[2]/div[1]/div/div[1]").click()
driver.find_element(By.XPATH, "//*[@id='mat-menu-panel-0']/div/button[2]").click()
#FirstName
driver.find_element(By.ID, "mat-input-2").clear()
driver.find_element(By.ID, "mat-input-2").send_keys("Prerna")
#LastName
driver.find_element(By.ID, "mat-input-8").clear()
driver.find_element(By.ID, "mat-input-8").send_keys("Singh")
#PhoneNumber
#driver.find_element(By.ID, "mat-input-3").clear()
#driver.find_element(By.ID, "mat-input-3").send_keys(i)
#Email
driver.find_element(By.ID, "mat-input-4").clear()
driver.find_element(By.ID, "mat-input-4").send_keys("prerna@demo.com")
#Address1
driver.find_element(By.ID, "mat-input-5").clear()
driver.find_element(By.ID, "mat-input-5").send_keys("XYZ road")
#Address2
driver.find_element(By.ID, "mat-input-6").clear()
driver.find_element(By.ID, "mat-input-6").send_keys("ASD")


#State

driver.find_element(By.NAME, "state").click()
driver.find_element(By.ID, "mat-option-16").click()
#driver.find_element_by_xpath("/html/body/app-root/layout/classy-layout/div/div[2]/app-user-profile/div/div[2]/div/div[1]/form/div/div/div[8]/mat-form-field/div/div[1]").click()
#drp = Select(driver.find_element(By.NAME, "state"))
#drp.select_by_visible_text(" Arunachal Pradesh ")

#Pincode
driver.find_element(By.ID, "mat-input-7").clear()
driver.find_element(By.ID, "mat-input-7").send_keys("111")
time.sleep(3)

#Save
driver.find_element(By.XPATH, "/html/body/app-root/layout/classy-layout/div/div[2]/app-user-profile/div/div[2]/div/div[2]/button[1]/span[1]").click()

#Logout
driver.find_element(By.XPATH, "/html/body/app-root/layout/classy-layout/fuse-vertical-navigation/div/div[2]/div[1]/div/div[1]").click()
driver.find_element(By.XPATH, "//*[@id='mat-menu-panel-0']/div/button[4]").click()

time.sleep(5)
driver.quit()

#time.sleep(5)
#driver.find_element_by_xpath("/html/body/app-root/layout/classy-layout/fuse-vertical-navigation/div/div[2]/fuse-vertical-navigation-collapsable-item[3]/div/div").click()
#driver.find_element_by_xpath("/html/body/app-root/layout/classy-layout/fuse-vertical-navigation/div/div[2]/fuse-vertical-navigation-collapsable-item[3]/div[2]/fuse-vertical-navigation-basic-item[1]/div/a").click()
#time.sleep(5)
#driver.find_element_by_id("mat-input-11").send_keys("5")
#driver.find_element_by_id("mat-input-12").send_keys("5")
#driver.find_element_by_id("mat-input-13").send_keys("5")
#driver.find_element_by_id("mat-input-14").send_keys("5")
