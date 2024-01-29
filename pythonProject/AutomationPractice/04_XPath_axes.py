from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/losers/bse/daily/groupa")

"""XPath Axes"""
"1. self "
"2. parent "
"3. Child "
"4. Ancestor "
"5. Descendant "
"6. Following "
"7. Following-sibling "
"8. Preceding "
"9. Preceding-sibling "

# self node

#text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Tejas Networks')]//self::a").text
text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Tejas Networks')]").text

print(text_msg)

childs = driver.find_elements(By.XPATH, "//a[contains(text(),'Tejas Networks')]/ancestor::tr/child::td")
print(len(childs))

ancestors = driver.find_element(By.XPATH, "//a[contains(text(),'Tejas Networks')]/ancestor::tr").text
print(ancestors)

descendants = driver.find_elements(By.XPATH, "//a[contains(text(),'Tejas Networks')]/ancestor::tr/descendant::*")
print("Length of descendants is : ", len(descendants))

followings = driver.find_elements(By.XPATH, "//a[contains(text(),'Tejas Networks')]/ancestor::tr/following::*")
print("Length of followings is : ", len(followings))

following_sib = driver.find_elements(By.XPATH, "//a[contains(text(),'Tejas Networks')]/ancestor::tr/following-sibling::tr")
print("Length of following siblings are : ", len(following_sib))

precedings = driver.find_elements(By.XPATH, "//a[contains(text(),'Tejas Networks')]/ancestor::tr/preceding::*")
print("Length of precedings is : ", len(precedings))

precedings_sib = driver.find_elements(By.XPATH, "//a[contains(text(),'Tejas Networks')]/ancestor::tr/preceding-sibling::tr")
print("Length of precedings siblings are : ", len(precedings_sib))

driver.quit()