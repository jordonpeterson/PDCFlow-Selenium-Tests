# I used this tutorial on POM for this unit https://www.youtube.com/watch?v=BURK7wMcCwU

from selenium import webdriver
import time
from google_pom import Google
import unittest


class GoogleSearch():
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        # Tells driver to search the DOM for up to 10 seconds before deciding
        #  that an element isn't there. This gives the element time to load
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def search_selenium(self):
        driver = self.driver
        google = Google(driver)

        google.navigate_to_google()

        google.enter_search_term('Selenium')

        google.google_search()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')
