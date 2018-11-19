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
    time.sleep(3)
    driver.find_element_by_xpath('//h3[1]/a').click()

    # Enter Email and Password into Facebook.com
    email = driver.find_element_by_id('email')
    email.send_keys(facebook_email)
    password = driver.find_element_by_id('pass')
    password.send_keys(facebook_password)
    driver.find_element_by_id('loginbutton').click()

    # Two Factor Authentication
    driver.find_element_by_id('u_0_f').click()
    driver.find_element_by_id('u_0_h').click()

    # Accept 6 digit text message code from user
    facebook_login_code = input()

    facebook_approvals_code_form = driver.find_element_by_id('approvals_code')
    facebook_approvals_code_form.send_keys(facebook_login_code)
    driver.find_element_by_id('checkpointSubmitButton').click()
    driver.find_element_by_id('u_0_3').click()
    driver.find_element_by_id('checkpointSubmitButton').click()


test_facebook_login(facebook_password='')
