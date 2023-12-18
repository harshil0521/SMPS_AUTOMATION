from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import logInScreen
import time
from transaction.dockCollection import fnDockCollection
from transaction.truckArrival import fnTruckArrival
from transaction.memberCollection import fnMemberCollection


# driver = webdriver.Chrome("C:/Driver/chromedriver.exe")

# driver = webdriver.Chrome()
s = Service("C:/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()


driver.implicitly_wait(10)
driver.get("http://dev.rmrd.in/#/login")
# driver.get('http://localhost:4200/#/login')
# driver.get('http://proc.smartmps.in/#/login')
# driver.get('http://uat.smartmps.in/#/login')

logInScreen.fnLogIn(driver)
fnMemberCollection(driver)
# fnTruckArrival(driver)
# fnDockCollection(driver)

time.sleep(2)
driver.quit()