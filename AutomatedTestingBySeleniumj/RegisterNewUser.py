from selenium import webdriver
import unittest
TARGET_URL=""


class RegisteNewUser(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)

        self.driver.get(TARGET_URL)


    def test_register_new_user(self):
        driver=self.driver
        driver.find_element_by_link_text("Log In").click()
        create_account_button=driver.find_element_by_xpath("//button[@title='Create an Account''")
        create_account_button.is_displayed()
        create_account_button.click()

        first_element=driver.find_element_by_id("first-name")

        \


