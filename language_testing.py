#!/usr/bin/python

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class LanguageTests (unittest.TestCase):
    def setUp (self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave'
        self.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=self.options)
        self.driver.maximize_window()

        self.driver.get("http://demo-store.seleniumacademy.com/")

    def test_select_language (self):
        exposed_options = ['English', 'French', 'German']
        active_options = []

        select_language = Select(self.driver.find_element_by_id("select-language"))

        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            active_options.append(option.text)

        self.assertListEqual(exposed_options, active_options)

        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text("German")
        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(self.driver.find_element_by_id("select-language"))
        select_language.select_by_index(0)

    def tearDown (self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
