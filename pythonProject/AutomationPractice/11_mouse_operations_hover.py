from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

"""Action chains class"""
# 1. Moues hover         move_to_element(element)
# 2. Right click         context_click(element)
# 3. Double click        double_click(element)
# 4. Drag and drop       drag_and_drop(source_element,target_element)
# 5. Slider              act.drag_and_drop_by_offset(element,increment for x axes in digit,
#                        increment for y axes in digit).perform()
# 6. Scrolling           execute_script()
"-------------------"
"""1. Mouse hover"""
"-------------------"

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-perform-mouse-hover-in-selenium.html")
# driver.implicitly_wait(5)

# button = driver.find_element(By.XPATH, "//button[@class='dropbtn']")
# sel = driver.find_element(By.XPATH, "//a[normalize-space()='Selenium']")

# act = ActionChains(driver)      # we have to create one action first and have to import ActionChains class

# act.move_to_element(button).move_to_element(sel).click().perform()  # start with act and end with perform is mandatory


"-------------------"
"""2. Right click"""
"-------------------"

# driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
# driver.implicitly_wait(5)
#
# button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
#
# act = ActionChains(driver)
#
# act.context_click(button).perform()


"-------------------"
"""3. Double click"""
"-------------------"

# driver.get("https://testautomationpractice.blogspot.com/")
# driver.implicitly_wait(5)
#
# button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
#
# act = ActionChains(driver)
#
# act.double_click(button).perform()


"-------------------"
"""4. Drag and drop"""
"-------------------"

# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# driver.implicitly_wait(5)

# source_ele = driver.find_element(By.ID, "box6")
# target_ele = driver.find_element(By.ID, "box106")

# act = ActionChains(driver)

# act.drag_and_drop(source_ele,target_ele).perform()

"-------------------"
"""5. Slider"""
"-------------------"

# driver.get("https://www.snapdeal.com/")
# driver.implicitly_wait(5)
# act = ActionChains(driver)
#
# search = driver.find_element(By.NAME, "keyword")
# search.send_keys("Shoes")
# search.send_keys(Keys.RETURN)
#
# min_slider = driver.find_element(By.XPATH, "//a[@class='price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
# max_slider = driver.find_element(By.XPATH, "//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
#
# print("Location of sliders before moving\n", min_slider.location, "\n", max_slider.location)
#
# # {'x': 73, 'y': 521}
# # {'x': 275, 'y': 521}
#
# act.drag_and_drop_by_offset(min_slider, 25, 0).perform()
# time.sleep(2)
# act.drag_and_drop_by_offset(max_slider, -25, 0).perform()
#
# print("\nNew Location of sliders before moving\n", min_slider.location, "\n", max_slider.location)

# {'x': 102, 'y': 437}
# {'x': 253, 'y': 435}


"-------------------"
"""6. Scrolling"""
"-------------------"


driver.get("https://www.snapdeal.com/")
driver.implicitly_wait(5)

# 1. Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,1500)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:", value)

# 2. Scroll down page till the element is visible
# img = driver.find_element(By.XPATH, "//i[@class='paymentIcon footerIconsImg']")
# driver.execute_script("arguments[0].scrollIntoView();", img)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:", value)

# 3. Scroll down page till end
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

# 4. Scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")

time.sleep(4)
driver.quit()


#  Till end

