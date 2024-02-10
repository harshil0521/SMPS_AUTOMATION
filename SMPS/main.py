from selenium import webdriver
import logInScreen, time
from transaction.dockCollection import fnDockCollection
from transaction.truckArrival import fnTruckArrival
from transaction.memberCollection import fnMemberCollection
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://dev.rmrd.in/#/login')
# driver.get('http://localhost:4200/#/login')
# driver.get('http://proc.smartmps.in/#/login')
# driver.get('http://uat.smartmps.in/#/login')

logInScreen.fnLogIn(driver)
# fnTruckArrival(driver)
# fnDockCollection(driver)
fnMemberCollection(driver)

time.sleep(2)
# driver.quit()