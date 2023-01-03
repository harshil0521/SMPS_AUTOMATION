from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# Ctrl + A
# Ctrl + C
# TAB
# Ctrl + V

driver.get("https://text-compare.com/")

input_1 = driver.find_element(By.ID, "inputText1")
input_2 = driver.find_element(By.ID, "inputText2")

input_1.send_keys("Welcome to selenium")

act = ActionChains(driver)


# input 1, ctrl + A
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

# copy, ctrl + C
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# tab
act.send_keys(Keys.TAB).perform()

# paste, ctrl + v
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
