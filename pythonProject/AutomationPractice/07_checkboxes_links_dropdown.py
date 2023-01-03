from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests as requests
import time

driver = webdriver.Chrome()
driver.maximize_window()

# """ Checkboxes """
#
# driver.get("https://itera-qa.azurewebsites.net/home/automation")
# # driver.find_element(By.ID, "monday").click()
# check_boxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
# print(len(check_boxes))
#
# """ Approach 1 """
# for i in range(len(check_boxes)):
#     check_boxes[i].click()
#
# """ Approach 2 """
# for box in check_boxes:
#     box.click()
#
# """ Approach 3: Select Multiple checkboxes by choice """
# for box in check_boxes:
#     week_name = box.get_attribute('id')
#     if week_name == 'monday' or week_name == 'wednesday':
#         box.click()
#
# """ Approach 4: Select last 2 checkboxes """
#
# x = len(check_boxes)
# for i in range(x-2, x):
#     check_boxes[i].click()
#
# """ Approach 5: Select first 2 checkboxes """
#
# x = len(check_boxes)
# for i in range(x):
#     if i < 2:
#         check_boxes[i].click()
#
# """ Clearing all checkboxes """
#
# for i in range(x):
#     if check_boxes[i].is_selected():
#         check_boxes[i].click()
#

# """ LINKS """
# # 1. internal
# # 2. external
# # 3. broken
#
# "----------------------------------------------------------------------"
# """ 1. internal links """
#
# driver.get("https://www.nopcommerce.com/en")
# # driver.find_element(By.LINK_TEXT, "Get started").click()
# # driver.find_element(By.PARTIAL_LINK_TEXT, "tarte").click()
#
# """Find total number of links in page """
# # links = driver.find_elements(By.TAG_NAME, 'a')
# # print("Total number of links by tag name : ", len(links))
#
# links = driver.find_elements(By.XPATH, "//a")
# print("Total number of links by XPATH name : ", len(links))
#
# """ Print all the links name """
# for link in links:
#     print(link.text)
#
#
"----------------------------------------------------------------------"
""" Broken links """
# The links which has no target page.
# If error code is >400 than it is a broken link, otherwise it is a normal link.

# ' Finding link how many links are broken '
# driver.get("http://www.deadlinkcity.com/")
# all_links = driver.find_elements(By.TAG_NAME, "a")
# count = 0
#
# for link in all_links:
#     url = link.get_attribute('href')
#     try:
#         response = requests.head(url)
#     except:
#         None
#
#     if response.status_code >= 400:
#         print(url, "is broken link.")
#         count += 1
#     else:
#         print(url, "is valid link.")
#
# print("Total number of broken links : ", count)
#



"----------------------------------------------------------------------"
#                            """ Dropdown """
"----------------------------------------------------------------------"

driver.get("https://www.opencart.com/index.php?route=account/register")
drp_country = Select(driver.find_element(By.NAME, "country_id"))
# drp_country.select_by_visible_text("India")         # most reliable
# drp_country.select_by_value("175")  # Romania
# drp_country.select_by_index(13)   # Australia

""" Finding all the option and print them """
all_options = drp_country.options
print("Total number of options : ", len(all_options))

for option in all_options:
    print(option.text)

# Select option from dropdown without built-in methods
for option in all_options:
    if option.text == "India":
        option.click()
        break

# https://testautomationpractice.blogspot.com/
# https://itera-qa.azurewebsites.net/home/automation

time.sleep(2)
driver.quit()
