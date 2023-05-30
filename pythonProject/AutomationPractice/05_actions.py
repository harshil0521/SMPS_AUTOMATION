import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

"""1. Application related get commands/method/function"""
"""2. Conditional commands"""
"""3. Browser commands"""
"""4. Navigational commands"""
"""5. Wait commands"""

"----------------------------------------------------------------------"
"""1. Application related get commands/method/function"""
"----------------------------------------------------------------------"
# Keywords/variables stored
    # 1. .get (Opening the application URL)
    # driver.get("https://www.nopcommerce.com/en/register?returnUrl=%2Fen%2Fdemo")

    # 2. title (To capture the title of current webpage)
    # print(driver.title)

    # 3. current_url (To capture the current url of page)
    # print(driver.current_url)

    # 4. page_source (To capture source code of the page)
    # print(driver.page_source)
"----------------------------------------------------------------------"
"""2. Conditional commands returns TRUE/FALSE"""
"----------------------------------------------------------------------"
# for checking the status of the elements
    # 1. is_displayed() "To check is particular element is available or not"
    # 2. is_enabled()   "To check element is enabled or disabled"
    # 3. is_selected()  "To check radio button & check box is selected or not"

    # search_box = driver.find_element(By.NAME, "srchword")
    # print("Display status : ", search_box.is_displayed())
    # print("Enabled status : ", search_box.is_enabled())

    # checking = driver.find_element(By.XPATH,"//label[normalize-space()='I would like to receive newsletters:']")
    # print(checking.is_selected())

"----------------------------------------------------------------------"
"""3. Browser commands"""
"----------------------------------------------------------------------"
# driver.close() "Close single browser window (where browser focused)"
# driver.quit()  "Killing the process of Chrome driver so all windows are closed"

"----------------------------------------------------------------------"
"""4. Navigational commands"""
"----------------------------------------------------------------------"
# back()
# forward()
# refresh()

driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.in/")
driver.back()   # snapdeal
time.sleep(3)
driver.forward()    # amazon
time.sleep(3)
driver.refresh()    # amazon
time.sleep(3)
driver.quit()
