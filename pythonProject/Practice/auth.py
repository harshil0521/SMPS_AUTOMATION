from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from main import driver
import unittest
from selenium import webdriver

driver = webdriver.Chrome()


def login(driver):
    driver.get("http://dev.rmrd.in/#/login")
    phone_number = driver.find_element(By.NAME, "phone_number")
    phone_number.clear()
    phone_number.send_keys("8160095599")

    password = driver.find_element(By.NAME, "password")
    password.clear()
    password.send_keys("1234")
    password.send_keys(Keys.RETURN)


