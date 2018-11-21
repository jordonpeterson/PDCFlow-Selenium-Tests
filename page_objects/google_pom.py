import time


class Google():

    def __init__(self, driver):
        self.driver = driver
        self.google_searchbox_name = 'q'
        self.google_searchbutton_name = 'btnK'

    def navigate_to_google(self):
        self.driver.get('https://www.google.com/')

    def enter_search_term(self, search_term):
        self.driver.find_element_by_name(self.google_searchbox_name).clear()
        self.driver.find_element_by_name(
            self.google_searchbox_name).send_keys(search_term)

    def hit_enter(self):
        self.driver.find_element_by_name(
        self.google_searchbox_name).send_keys(u'\ue007')

    def google_search(self):
        # The time.sleep method allows the page to refresh before we find the searchbox.
        # It would be better to use one of the await element methods here.
        time.sleep(2)
        print('google_search')
        search_button = self.driver.find_element_by_name(
            self.google_searchbox_name)
        print('search button found')
        time.sleep(2)
        search_button.click()

        print('button clicked')
        time.sleep(5)
