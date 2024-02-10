from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from logInScreen import fnLogIn
from transaction.memberCollection import fnMemberCollection
from transaction.truckArrival import fnTruckArrival
from transaction.dockCollection import fnDockCollection
from transaction.labCollection import fnLabCollection
from transaction.tankerDispatch import fnTankerDispatch
from transaction.tankerReceive import fnTankerReceive
from master.memberMaster import fnMemberMaster
from master.mppMaster import fnMPPMaster
import time

# driver = webdriver.Chrome("C:/Driver/chromedriver.exe")
# driver = webdriver.Chrome()

serv = Service("C:/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.maximize_window()

# URL = 'https://uat.smartmps.in/#/login'
# URL = 'http://dev.rmrd.in/#/login'
# URL = 'http://localhost:4200/#/login'
URL = 'http://proc.smartmps.in/#/login'

driver.get(URL)
driver.implicitly_wait(10)

fnLogIn(driver)

# fnMemberCollection(driver)
# fnTruckArrival(driver)
# fnDockCollection(driver)
# fnLabCollection(driver)
# fnTankerDispatch(driver)
# fnTankerReceive(driver)
# fnMemberMaster(driver)
fnMPPMaster(driver)

time.sleep(2)
driver.quit()
