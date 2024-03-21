from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import random

# driver = webdriver.Chrome("C:/Driver/chromedriver.exe")
serv = Service("C:/Driver/geckodriver.exe")
driver = webdriver.Firefox(service=serv)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://poshanabhiyaan.gov.in/addactivityparticipation')
time.sleep(5)
driver.find_element(By.NAME, 'username').send_keys('mow&cd-2445810')
driver.find_element(By.NAME, 'password').send_keys('mow&cd-2445810')
driver.find_element(By.CLASS_NAME, 'submit_button_box').click()

for x in range(1):

    """Select Theme and Activity"""
    themeNumber = random.randint(1, 10)

    def chooseActivity(themeNumber):
        if themeNumber == 1:
            activityNumber = random.randint(1, 5)
        elif themeNumber == 2:
            activityNumber = random.randint(12, 15)
        elif themeNumber == 3:
            activityNumber = random.randint(16, 24)
        elif themeNumber == 4:
            activityNumber = random.randint(25, 28)
        elif themeNumber == 5:
            activityNumber = random.randint(31, 37)
        elif themeNumber == 6:
            activityNumber = random.randint(43, 50)
        elif themeNumber == 7:
            activityNumber = random.randint(51, 56)
        elif themeNumber == 8:
            activityNumber = random.randint(59, 65)
        elif themeNumber == 9:
            activityNumber = random.randint(67, 69)
        elif themeNumber == 10:
            activityNumber = random.randint(73, 89)
        return activityNumber;

    activityNumber = chooseActivity(themeNumber)

    """Select Theme"""
    theme = Select(driver.find_element(By.NAME, "SelectTheme"))
    theme.select_by_value(str(themeNumber))

    """Select Level"""
    level = Select(driver.find_element(By.NAME, "SelectLevel"))
    level.select_by_value("5")

    """Select AWC"""
    awc = Select(driver.find_element(By.NAME, 'awc_center'))
    awc.select_by_value("133535")

    """Select Activity"""
    activity = Select(driver.find_element(By.NAME, 'SelectActivity'))
    activity.select_by_value(str(activityNumber))

    """Select Date"""
    driver.find_element(By.NAME, "SelectDateFrom").send_keys('2024-03-21')
    driver.find_element(By.NAME, "SelectDateTo").send_keys('2024-03-21')

    """Count of People"""
    driver.find_element(By.NAME, "CountAdultMale").send_keys("15")
    driver.find_element(By.NAME, "CountAdultFemale").send_keys("15")
    driver.find_element(By.NAME, "CountChildMale").send_keys("15")
    driver.find_element(By.NAME, "CountChildFemale").send_keys("15")

    """Saving Data"""
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
    print(x + 1, 'Theme number-', themeNumber, 'Activity Number-', activityNumber)
    driver.refresh()

driver.quit()
