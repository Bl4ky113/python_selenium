#!/usr/bin/python

import unittest
from selenium import webdriver

class Tests (unittest.TestCase):
    def setUp (self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave'
        self.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=self.options)
        self.driver.maximize_window()

        self.driver.get("https://the-internet.herokuapp.com/tables")

    def test_get_table_info (self):
        categories = len(self.driver.find_elements_by_css_selector('#table1 > thead > tr > th')) - 1
        size_table = len(self.driver.find_elements_by_css_selector('#table1 > tbody > tr'))
        table = {}

        for i in range(categories):
            category = self.driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span').text
            table[category] = []

            for j in range(size_table):
                table[category].append(self.driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]').text)

        print(table)

    def tearDown (self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)

