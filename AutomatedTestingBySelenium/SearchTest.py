import unittest
from selenium import webdriver

TARGET_URL="https://github.com"

class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(TARGET_URL)
    def test_search(self):
        self.form_textfield = self.driver.find_element_by_name("q")
        self.form_textfield = self.driver.find_element_by_name("q")
        # 入力フォームに，”hoge”と入力する
        self.form_textfield.send_keys("hoge")
        # 入力した内容を削除する
        #form_textfield.clear()
        # 入力したキーワード("hoge")を送信し，検索を実行する
        self.form_textfield.submit()
        

    def calc_start_time(self):
        print()
    def calc_end_time(self):
        print()

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
  unittest.main()