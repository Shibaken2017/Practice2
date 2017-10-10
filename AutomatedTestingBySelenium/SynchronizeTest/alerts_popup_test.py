'''
jsのアラートが出るか
'''

from selenium.webdriver.support.ui import Select
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest
#jsのexampleサイト
TARGET_URL="http://www.tagindex.com/javascript/window/confirm.html"



driver=webdriver.Firefox()
driver.implicitly_wait(30)

driver.maximize_window()
driver.get(TARGET_URL)

#[@class="header"]
search_field=driver.find_element_by_xpath('//input[@value="確認ダイアログ"]')

search_field.click()
#alert画面object
alert=driver.switch_to_alert()

alert_text=alert.text
print(alert.text)

alert.accept()

print(driver.current_url)