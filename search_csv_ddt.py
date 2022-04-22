#!/usr/bin/python

import unittest
import csv
from ddt import ddt, data, unpack
from selenium import webdriver

def get_data (file_name):
    rows = []

    with open(file_name, 'r', encoding="UTF-8") as data_file:
        reader = csv.reader(data_file)
        next(reader, None)

        for row in reader:
            rows.append(row)

    return rows

@ddt
class Tests (unittest.TestCase):
    def setUp (self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave'
        self.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=self.options)
        self.driver.maximize_window()

        self.driver.get("http://demo-store.seleniumacademy.com/")

    @data (*get_data('./ddt_data.csv'))
    @unpack

    def test_search_csv (self, search_value, expected_count):
        search_bar = self.driver.find_element_by_name('q')
        search_bar.clear()
        search_bar.send_keys(search_value)
        search_bar.submit()

        products = self.driver.find_elements_by_css_selector('body > div > div.page > div.main-container.col3-layout > div > div.col-wrapper > div.col-main > div.category-products > ul > li')

        if int(expected_count) > 0:
            self.assertEqual(len(products), int(expected_count))
        else:
            error_msg = self.driver.find_elements_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.', error_msg.text)

    def tearDown (self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
