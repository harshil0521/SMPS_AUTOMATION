import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()


def chrome_setup():
    # download file in desired location
    preference = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", preference)
    driver = webdriver.Chrome(options=options)
    return driver


def edge_setup():
    # download file in desired location
    preference = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
    options = webdriver.EdgeOptions()
    options.add_experimental_option("prefs", preference)
    driver = webdriver.Edge(options=options)
    return driver


def firefox_setup():
    # download file in desired location
    options = webdriver.FirefoxOptions()
    options.set_preference("browser.helperApps.neverAsk. saveToDisk", "application/msword")
    # Mime types : https://www.sitepoint.com/mime-types-complete-list/ For file choose correct Mime type
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.folderList", 2)  # 0-desktop 1-downloads folder 2- Desired folder
    options.set_preference("browser.download.dir", location)
    options.set_preference("pdfjs.disabled", True)  # for PDF
    driver = webdriver.Firefox(options=options)
    return driver


# Automation code
my_driver = chrome_setup()
# my_driver = edge_setup()
my_driver.get("https://file-examples.com/index.php/sample-documents-download/")
time.sleep(10)
my_driver.find_element(By.XPATH, "//a[@href='https://file-examples.com/index.php/sample-documents-download/sample-doc-download/']").click()
