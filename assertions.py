#!/usr/bin/python

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By # Bl4ky113

class AssertionsTests (unittest.TestCase):
    def setUp (self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave'
        self.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=self.options)
        self.driver.maximize_window()

        self.driver.get("http://demo-store.seleniumacademy.com/")

    def test_search_field (self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_options (self):
        self.assertTrue(self.is_element_present(By.ID, "select-language"))

    def tearDown (self):
        self.driver.quit()

    def is_element_present (self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False

        return True

if __name__ == "__main__":
    unittest.main(verbosity=2)
