#!/usr/bin/python

import unittest
from ddt import ddt, data, unpack
from selenium import webdriver

@ddt
class DataDrivenTests (unittest.TestCase):
    def setUp (self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave'
        self.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=self.options)
        self.driver.maximize_window()

        self.driver.get("http://demo-store.seleniumacademy.com/")

    @data (('dress', 5), ('music', 5))
    @unpack

    def test_search_ddt (self, search_value, expected_count):
        search_bar = self.driver.find_element_by_name("q")
        search_bar.clear()
        search_bar.send_keys(search_value)
        search_bar.submit()

        products = self.driver.find_elements_by_css_selector('body > div > div.page > div.main-container.col3-layout > div > div.col-wrapper > div.col-main > div.category-products > ul > li')
        self.assertEqual(len(products), expected_count)

    def tearDown (self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
