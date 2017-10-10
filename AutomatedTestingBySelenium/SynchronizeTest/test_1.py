import unittest
from selenium  import webdriver
target_url="https://www.google.co.jp/"



class SearchProductTEst(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.driver.maximize_window()
        self.driver.get(target_url)

    def test_search(self):
        search_field=self.driver.find_element_by_id("lst-ib")
        print(search_field)
        self.assertEqual("2","2")

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()

