from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.nopcommerce.com/en")

"Full form is XML Path."
    # Extensible Markup Language
"XPath is a syntax or language for finding any element on the webpage using XML path expression."
"It is user to find the location of any element on a webpage using HTML DOM structure."
    # DOM = Document Object Model.
    # DOM is an API Interface provided by browser.
    # When webpage is loaded, the browser creates a Document Object Model of the page.

"It can be used to navigate through elements and attributes in DOM."
"It is an address of the element."

# Types of XPATH
"1. Absolute/Full xpath"
    # Ex - /html/body/nav/div/div/div[2]/ul/li[1]/a/button
"2. Relative/Partial xpath"
    # Ex - //*[@id="navbarSupportedContent"]/div[2]/ul/li[1]/a/button

# Difference
"1.  Absolute Xpath starts from root html node."
"    Relative xpath directly jump to element on DOM."
"2.  Absolute Xpath starts with /."
"    Relative Xpath starts with //."
"3.  In Absolute Xpath we use only tag/node."
"    In Relative Xpath we use attributes. //."


# How to write XPATH manually

"1. To write absolute xpath start from bottom to top."

"2. To write relative xpath follow syntax."
# "syntax : driver.find_element(By.XPATH, "//tag name[@attribute= 'value of attribute']")
# "Ex. : driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# "Ex. : driver.find_element(By.XPATH, "//*[@id='small-searchterms']")

# How to capture xpath automatically
"1. Right click on element > Inspect > Highlight HTML code > Right click > Copy > Copy XPath"
"2. SelectorsHub extension "

"1. If developers adds new element then Absolute XPath will be broken."
"2. If developers change the location then Absolute XPath will be broken."
"3. Relative XPath is more stable than Absolute XPath"
"4. Absolute XPath is lengthy in compare to Relative XPath."

# xpath options
"1. and "
"2. or "
"3. contains() "
"4. starts-with() "
"5. text() "


"""XPath with OR"""
driver.find_element(By.XPATH, "//tag name[@attribute= 'value of attribute' or @attribute= 'value of attribute']")
# any one attribute should match


"""XPath with AND"""
driver.find_element(By.XPATH, "//tag name[@attribute= 'value of attribute' and @attribute= 'value of attribute']")
# both attribute should match

""" contains() or starts-with """

# contains() method check that the given value of attribute is containing or not in any place.
# start button -> xpath is //*[@id='start']
# stop button  -> xpath is //*[@id='stop']
# same button  -> xpath is //*[contains(@id,'st')]

# same button  -> xpath is //*[@id='start' or @id='stop']

# starts-with method check that the given value of attribute is containing or not at starting point.
# start button -> xpath is //*[@id='start']
# stop button  -> xpath is //*[@id='stop']
# same button  -> xpath is //*[starts-with(@id,'st')]

""" text() """
driver.find_element(By.XPATH, "tagname[text()='value of need']")