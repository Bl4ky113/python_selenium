#!/usr/bin/python

import unittest
from selenium import webdriver

class ExtraTests (unittest.TestCase):
    def setUp (self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave'
        self.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=self.options)
        self.driver.maximize_window()

        self.driver.get("http://demo-store.seleniumacademy.com/")
 
    def test_search_hell (self):
        search_input = self.driver.find_element_by_name("q")
        search_input.clear()
        search_input.send_keys("hell")
        search_input.submit()

        products = self.driver.find_elements_by_class_name("item")
        self.assertEqual(2, len(products))

    def test_check_bags_prices (self):
        search_input = self.driver.find_element_by_name("q")
        search_input.clear()
        search_input.send_keys("bag")
        search_input.submit()

        bags = self.driver.find_elements_by_xpath('//*[@id="product-minimal-price-439"]')
        for bag in bags:
            self.assertGreaterEqual(int(bag.text[1:-3]), 600)

    def tearDown (self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
