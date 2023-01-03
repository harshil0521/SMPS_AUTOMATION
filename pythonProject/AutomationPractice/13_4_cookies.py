from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Capture cookies from the browser # Every cookie have attributes, dictionary collection
cookies = driver.get_cookies()
print("original length\t",len(cookies))

#for c in cookies:
    #   print(c)                                    # Print all data
    #   print(c.get("name"))                        # Print only name
    #   print(c.get("name"),":",c.get("expiry"))        # Print name and expiry


"--------------------------"
"""How to add new cookie"""
"--------------------------"
driver.add_cookie({"name": "my_cookie", "value": "123"})
cookies = driver.get_cookies()
print("after adding new\t", len(cookies))


"--------------------------"
"""How to delete cookie"""
"--------------------------"
driver.delete_cookie("my_cookie")
cookies = driver.get_cookies()
print("after deleting\t", len(cookies))

"--------------------------"
"""How to delete all cookies"""
"--------------------------"
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("after deleting all\t", len(cookies))


driver.quit()

