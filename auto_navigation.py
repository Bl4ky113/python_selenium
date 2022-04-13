#!/usr/bin/python

import unittest
from selenium import webdriver

class NavigationTests (unittest.TestCase):
    def setUp (self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave'
        self.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=self.options)
        self.driver.maximize_window()

        self.driver.get("http://search.brave.com/")

    def test_browser_navigation (self):
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('Platzi')
        search_field.submit()

        self.driver.back()
        self.driver.forward()
        self.driver.refresh()

    def tearDown (self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
