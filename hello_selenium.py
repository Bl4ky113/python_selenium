#!/usr/bin/python

import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld (unittest.TestCase):
    @classmethod
    def setUp (cls):
        cls.options = webdriver.ChromeOptions()
        cls.options.binary_location = '/usr/bin/brave'
        cls.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=cls.options)

        cls.driver.implicitly_wait(10)

    def test_hello_world (self):
        self.driver.get('https://www.brave.com')

    def test_visit_invidious (self):
        self.driver.get('https://www.invidio.us')

    @classmethod
    def tearDown (cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="./", report_name="hello_world_report"))
