from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
driver.maximize_window()


"--------------"
"""Web table"""
"--------------"
# 1. Static webtable
# 2. Dynamic webtable

# 1) Count number of rows & columns
# 2) Read specific row & column data
# 3) Read alt the rows & columns data
# 4) Read date based on condition(List all books name whose author is Mukesh)



# 1) Count number of rows & columns

# data = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
# for i in data:
#     print(i.text)

no_OF_raw = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
# print(no_OF_raw)  #7
#
no_OF_col = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
# print(no_OF_col)


# 2) Read specific row & column data

# data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(data)


# 3) Read alt the rows & columns data
"""Modifying XPath"""
# data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text

# data = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
# print("\nPrinting table")
# for r in range(2, no_OF_raw+1):
#     for c in range(1, no_OF_col+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data, end='      ')
#     print()

# 4) Read date based on condition(List all books name whose author is Mukesh)

for r in range(2, no_OF_raw+1):
    author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author_name == "Mukesh":
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(author_name, " ", book_name, price)

driver.close()  #4
