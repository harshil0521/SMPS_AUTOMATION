import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# alerts are not web elements
"""object = driver.switch_to.alert"""
# 1. object.text
# 2. object.accept()
# 2. object.dismiss()


driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# opens alert window
# driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
# time.sleep(2)
#
# alert_window = driver.switch_to.alert   # learned
# print(alert_window.text)
# alert_window.send_keys("Welcome to this method.")
# # alert_window.accept()   # close by ok
# alert_window.dismiss()  # close by cancel


# driver.get("https://mypage.rediff.com/login/dologin")

# login = driver.find_element(By.XPATH, "//input[@value='Login']")
# login.click()
# time.sleep(2)
# driver.switch_to.alert.accept()

"----------------------------"
"""Authentication pop-up"""
"----------------------------"
#  the concept of injection
"syntax : https://username:password@url"

# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")


"---------------------------------------------------------"
"Frames (windows application) / IFrames (web application)"
"---------------------------------------------------------"
# tagnames - frame/iframe/form
# driver.switch_to_frame()    -selenium 3

#  -selenium 4
# switch_to.frame("name of the frame")
# switch_to.frame("id of the frame")
# switch_to.frame(webelement)
# switch_to.frame(0)
# switch_to.default_content()


# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
#
# driver.switch_to.frame("packageListFrame")
# driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
# driver.switch_to.default_content()      # go back to main page
#
# driver.switch_to.frame("packageFrame")
# driver.find_element(By.LINK_TEXT, "WebDriver").click()
# driver.switch_to.default_content()
# driver.switch_to.parent_frame()
# driver.switch_to.frame("classFrame")
# driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()



""" inner frame"""

driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

first_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(first_frame)    # outer frame

second_frame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(second_frame)    # inner frame
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")

driver.switch_to.parent_frame()     # from inner to outer frame



# time.sleep(2)
# driver.quit()