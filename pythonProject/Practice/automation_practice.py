from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Prerna Singh\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
element = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
element.clear()
element.send_keys("Python")
element.send_keys(Keys.RETURN)
time.sleep(3)
driver.quit()

#NewWindows
#wiki = driver.find_element_by_class_name("wikipedia-search-input")
#wiki.send_keys("selenium")
#wiki.send_keys(Keys.RETURN)
#driver.find_element_by_class_name("wikipedia-search-button").click()
#time.sleep(1)

#Alert
#driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
#Alert(driver).accept()
#Alert(driver).dismiss()

#DatePicker

#DoubleClick
#time.sleep(1)
#driver.find_element_by_id("field1").clear()
#driver.find_element_by_id("field1").send_keys("Testing for double click")
#element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
#action = ActionChains(driver)
#action.double_click(element).perform()
#time.sleep(1)

#FirstName
#driver.find_element_by_id("RESULT_TextField-1").send_keys("Harshil")


#time.sleep(3)
#driver.quit()