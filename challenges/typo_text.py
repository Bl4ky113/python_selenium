#!/usr/bin/python

import unittest
from selenium import webdriver

class Tests (unittest.TestCase):
    def setUp (self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave'
        self.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=self.options)
        self.driver.maximize_window()

        self.driver.get("https://the-internet.herokuapp.com/typos")

    def test_check_fix_typo (self):
        correct_text = """Sometimes you'll see a typo, other times you won't."""
        check_text = self.driver.find_element_by_css_selector('#content > div > p:nth-child(3)').text
        tries = 1

        while True:
            if check_text == correct_text:
                print("Tries: ", tries)
                break

            check_text = self.driver.find_element_by_css_selector('#content > div > p:nth-child(3)').text
            self.driver.refresh()
            tries += 1

    def tearDown (self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
