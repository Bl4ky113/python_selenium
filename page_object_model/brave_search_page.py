#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BravePage (object):
    def __init__ (self, driver):
        self._driver = driver
        self._url = "https://search.brave.com/"
        self.search_locator = 'q'

    @property
    def is_loaded (self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, self.search_locator)
            )
        )
        return True

    @property
    def keyword (self):
        input_search = self._driver.find_element_by_name(self.search_locator)
        return input_search.get_attribute('value')

    def open (self):
        self._driver.get(self._url)

    def type_search (self, keyword):
        input_search = self._driver.find_element_by_name(self.search_locator)
        input_search.send_keys(keyword)

    def click_submit (self):
        input_search = self._driver.find_element_by_name(self.search_locator)
        input_search.submit()

    def search (self, keyword):
        self.type_search(keyword)
        self.click_submit()
