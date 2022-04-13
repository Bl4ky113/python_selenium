#!/usr/bin/python

import unittest
from csv import reader as csv_reader
from selenium import webdriver

class Tests (unittest.TestCase):
    def setUp (self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave'
        self.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=self.options)
        self.driver.maximize_window()

        self.user_data = []
        with open('./users_data.csv', newline='', encoding="UTF-8") as csv_file:
            csv_content = csv_reader(csv_file, delimiter=",")
            for content in csv_content:
                self.user_data.append(content[0])
                self.user_data.append(content[1])
                self.user_data.append(content[2])
                self.user_data.append(content[3])

        self.user_data = tuple(self.user_data)


        self.driver.get("http://demo-store.seleniumacademy.com/")\

    def test_new_user (self):
        self.driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a').click()
        self.driver.find_element_by_xpath('//*[@id="header-account"]/div/ul/li[5]/a').click()

        self.assertEqual(self.driver.title, 'Create New Customer Account')

        self.driver.find_element_by_name('firstname').send_keys(self.user_data[0])
        self.driver.find_element_by_name('lastname').send_keys(self.user_data[1])
        self.driver.find_element_by_name('email').send_keys(self.user_data[2])
        self.driver.find_element_by_name('password').send_keys(self.user_data[3])
        self.driver.find_element_by_name('confirmation').send_keys(self.user_data[3])

        self.driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button').submit()

        self.assertEqual(self.driver.title, 'My Account')

    def tearDown (self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
