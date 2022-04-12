#!/usr/bin/python

import unittest
from selenium import webdriver

class Tests (unittest.TestCase):
    def setUp (self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave'
        self.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=self.options)
        self.driver.maximize_window()

        self.driver.get("http://demo-store.seleniumacademy.com/")
    
    def tearDown (self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
