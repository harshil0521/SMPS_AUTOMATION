# Advantages
# 1. Multiple class parallel
# 2. Execution will be very fast

from selenium import webdriver


def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(options=ops)
    return driver


my_driver = headless_chrome()
my_driver.get("https://demo.nopcommerce.com/")
print(my_driver.title)
print(my_driver.current_url)
my_driver.close()
