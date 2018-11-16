# Imports
from selenium import webdriver
import sys
import time


def test_google_selenium(browser):
    "Test Google Selenium"

    # Create an instance of WebDriver I will assume we are using FireFox
    if browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    # Alert user if they are not using Firefox
    else:
        print('We need to use the Firefox Browser for this test')

    # Variables used for Assert Statement
    total_tests = 2
    passed_tests = 0

    # Navigate to google.com
    driver.get('https://www.google.com/')

    # Find the searchbox by name
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('selenium')
    # Press Enter
    search_box.send_keys(u'\ue007')

    # Find the Selenium Link
    time.sleep(2)
    selenium_site = driver.find_element_by_xpath(
        '//*[@id="rso"]/div[1]/div/div/div/div[1]/a/h3')
    selenium_site.click()

    # Test that we are at the correct URL.
    time.sleep(5)
    if (driver.current_url == "https://www.seleniumhq.org/"):
        passed_tests += 1
        print('This is the correct URL')
    else:
        print('The URL is not correct')

    # Test that this URL is actually about Selenium
    if ('Selenium' in driver.title):
        passed_tests += 1
        print('The page title contains Selenium')
    else:
        print('The page title does not contain Selenium')

    # Check if all tests were passed
    assert total_tests == passed_tests
    print('all tests passed')

    # print(f"{passed_tests} out of {total_tests} passed.")
    # The above line is python 3.6+ syntax that prints how many tests were passed.
    # It is not included in the Python 2.7 that I am using in this environment.

    # Exit Browser
    time.sleep(2)
    driver.quit()


test_google_selenium('firefox')
# # Copied from https://qxf2.com/blog/modify-python-gui-automation-use-pytest/
# if __name__ == '__main__':
#     browser = sys.argv[1]
#     test_google_selenium(browser)
