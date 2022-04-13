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

    def test_compare_products_removal_alert (self):
        search_bar = self.driver.find_element_by_name('q')
        search_bar.clear()
        search_bar.send_keys('tee')
        search_bar.submit()

        self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[3]/div/div[2]/div/a').click()

        alert = self.driver.switch_to.alert
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert.text)
        alert.accept()

    
    def tearDown (self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
