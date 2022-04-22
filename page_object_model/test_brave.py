#!/usr/bin/python

import unittest
from selenium import webdriver
from brave_search_page import BravePage

class BraveTests (unittest.TestCase):
    @classmethod
    def setUp (cls):
        cls.options = webdriver.ChromeOptions()
        cls.options.binary_location = '/usr/bin/brave'
        cls.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=cls.options)
        cls.driver.maximize_window()

    def test_search (self):
        brave = BravePage(self.driver)

        brave.open()
        self.assertTrue(brave.is_loaded)
        brave.search('Hello World')
        self.assertEqual('Hello World', brave.keyword)

    @classmethod
    def tearDown (cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
