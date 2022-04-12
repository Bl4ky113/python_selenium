#!/usr/bin/python

import unittest
from selenium import webdriver

class HomePageTests (unittest.TestCase):
    def setUp (self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/brave'
        self.driver = webdriver.Chrome(executable_path='/home/bl4ky113/bin/chromedriver', options=self.options)

        self.driver.get("http://demo-store.seleniumacademy.com/")
        self.driver.maximize_window()

    def test_search_textfield (self):
        search_input = self.driver.find_element_by_id("search")

    def test_search_button_enabled (self):
        search_btn = self.driver.find_element_by_class_name("search-button")

    def test_count_images_promo_banner (self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banners))

    def test_vip_promo (self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[3]/a/img')
    
    def tearDown (self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
