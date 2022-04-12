#!/usr/bin/python

import unittest
from selenium import webdriver

class SearchTests (unittest.TestCase):
    def setUp (self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave'
        self.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=self.options)
        self.driver.maximize_window()

        self.driver.get("http://demo-store.seleniumacademy.com/")

    def test_search_tee (self):
        search_input = self.driver.find_element_by_name("q")
        search_input.clear()
        search_input.send_keys('tee')
        search_input.submit()

    def test_search_salt_shaker (self):
        search_input = self.driver.find_element_by_name("q")
        search_input.clear()
        search_input.send_keys("salt shaker")
        search_input.submit()

        products = self.driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li[1]/div/h2/a')
        self.assertEqual(1, len(products))
    
    def tearDown (self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
