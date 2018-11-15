from selenium import webdriver


# I will assume we are using the FireFox driver.
def test_google_selenium(browser):
    "Test Google Selenium"

    # Create an instance of WebDriver
    if browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    # Alert user if they are not using Firefox
    else:
        print('We need to use the Firefox Browser for this test')

    # Navigate to google.com
    driver.get('https://www.google.com/')

    # Find the searchbox by name
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('selenium')

    # Find the Google Search button by name and click it
    google_search = driver.find_element_by_name('btnk')
    google_search.click()

    # Find the Selenium Link
    selenium_site = driver.find_elements_by_link_text(
        'Selenium - Web Browser Automation')
    selenium_site.click()

    # Test that we are at the correct URL.
    assert driver.current_url == "https://www.seleniumhq.org/"
    # Test that this URL is actually about Selenium
    assert 'Selenium' in driver.title
    print('Test Ran')
    # Exit Browser
    driver.quit()
