import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\Prerna Singh\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#NewWindows
wiki = driver.find_element(By.CLASS_NAME,"wikipedia-search-input")
wiki.send_keys("Samudra Tech")
wiki.send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element(By.CLASS_NAME,"wikipedia-search-button").click()

#Alerts
driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()
#Alert(driver).accept()
Alert(driver).dismiss()


#DatePicker
driver.find_element(By.ID,"datepicker").click()

#Volunteer
#friend = driver.find_element(By.ID, "RESULT_TextField-1")
#friend.send_keys("Harshil")
#driver.find_element(By.ID, "RESULT_TextField-2").send_keys("Solanki")
#driver.find_element(By.ID, "RESULT_TextField-3").send_keys("8141338462")
#driver.find_element(By.ID, "RESULT_TextField-4").send_keys("India")
#driver.find_element(By.ID, "RESULT_TextField-5").send_keys("Ahmedabad")
#driver.find_element(By.ID, "RESULT_TextField-6").send_keys("harshil.solanki@samudratech.com")

#DoubleClick
#dc = driver.find_element(By.ID, "field1")
#dc.clear()
#dc.send_keys("Bicheck")
#ele = driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")
#action = ActionChains(driver)
#action.double_click(ele).perform()

time.sleep(3)
#driver.close()
