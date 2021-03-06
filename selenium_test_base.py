#!/usr/bin/python

import unittest
from selenium import webdriver

class Tests (unittest.TestCase):
    @classmethod
    def setUp (cls):
        cls.options = webdriver.ChromeOptions()
        cls.options.binary_location = '/usr/bin/brave'
        cls.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=cls.options)
        cls.driver.maximize_window()

        cls.driver.get("http://demo-store.seleniumacademy.com/")
    
    @classmethod
    def tearDown (cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
