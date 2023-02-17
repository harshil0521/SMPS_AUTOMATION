from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def fn_log_in(driver):
    """Number & Password"""
    phone_number = driver.find_element(By.NAME, "phone_number")
    phone_number.clear()
    password = driver.find_element(By.NAME, "password")
    password.clear()

    """Live admin"""
    # phone_number.send_keys("8141000000")
    # password.send_keys("123")

    """Live BMC Collection"""
    phone_number.send_keys("8160095599")
    password.send_keys("123")

    password.send_keys(Keys.RETURN)

    """Dock & Shift selection"""
    dock_dropdown = driver.find_element(By.NAME, "dock")
    dock_dropdown.click()

    dock_selection = driver.find_element(By.ID, "mat-option-2")
    dock_selection.click()

    # date_selection = driver.find_element() TODO calender script
    # date_calender = driver.find_element(By.XPATH, "//button[@aria-label='Open calendar']")
    # date_calender.click()
    # time.sleep(3)

    shift = driver.find_element(By.NAME, "shift")
    shift.click()

    selected_shift = driver.find_element(By.XPATH, "//*[contains(text(), 'Morning')]")
#   selected_shift = driver.find_element(By.XPATH, "//*[contains(text(), 'Evening')]")
    selected_shift.click()

    submit = driver.find_element(By.XPATH, "//*[contains(text(), 'Submit')]")
    submit.click()
    time.sleep(0.5)
