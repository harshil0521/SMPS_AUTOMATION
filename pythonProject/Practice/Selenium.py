from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Prerna Singh\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://www.google.com/")
driver.maximize_window()
element = driver.find_element(By.NAME, "q")
#element = driver.find_element_by_name("search_query")
element.clear()
element.send_keys("Selenium using python")
element.send_keys(Keys.RETURN)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable(By.CLASS_NAME, 'LC20lb MBeuO DKV0Md'))
element.click()
#driver.find_element(By.CLASS_NAME, 'NqpkQc')


#time.sleep(5)
#driver.quit()

