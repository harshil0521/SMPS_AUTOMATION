from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.implicitly_wait(10)
# How to get window ID # randomly created by browser
# driver.current_window_handle()   # this will return WindowID of current window
# window_handles                   # this will return WindowID of multiple windows

# driver.switch_to.window("Window id")

# window_id = driver.current_window_handle
# print(window_id)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowIDs = driver.window_handles
print("Parent window id :", windowIDs[0], "\nChild window id :", windowIDs[1])

driver.switch_to.window(windowIDs[1])
print("child", driver.title)

driver.switch_to.window(windowIDs[0])
print("parent", driver.title)

driver.quit()

for win in windowIDs:
    driver.switch_to.window(win)
    print(driver.title)
