# imports
from selenium import webdriver
import time
import sys


def test_facebook_login(facebook_email='jordon.peterson@students.svu.edu', facebook_password='dontyouwishyouknew'):
    "Test Facebook Login"

    # Create driver and set up initial variables.
    driver = webdriver.Firefox()

    total_tests = 0
    passed_tests = 0

    # Navigate from Google to Facebook.com
    driver.get('https://www.google.com/')
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('facebook')
    time.sleep(1)
    google_search = driver.find_element_by_name('btnK')
    google_search.click()


test_facebook_login()
