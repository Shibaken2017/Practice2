from  selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest

TARGET_URL=""
class ExplicitWaitTests(unittest.TestCase):
    def setUP(self):
        self.driver=webdriver.Firefox()
        self.driver.get(TARGET_URL)


    def test_account_link(self):
        WebDriverWait.(self.driver,10).until(expected_conditions.invisibility_of_element_located(By.LI))