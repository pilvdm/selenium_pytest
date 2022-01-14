"""
This is a page object for GOOGLE title and search pages united (for simplicity)
"""


from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchLocators:

    LOCATOR_GOOGLE_SEARCH_FIELD = (By.NAME, "q")
    LOCATOR_GOOGLE_NAVIGATION_BAR = (By.CSS_SELECTOR, ".hdtb-mitem")
    LOCATOR_GOOGLE_SEARCH_RESULT_LINKS = (By.CSS_SELECTOR, ".g a")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.send_keys(word)
        return search_field

    def perform_search(self):
        return self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_FIELD).send_keys(Keys.ENTER)

    def check_navigation_bar(self):
        navbar_elements = self.find_elements(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION_BAR, time=2)
        nav_bar_menu = [x.text for x in navbar_elements if len(x.text) > 0]
        return nav_bar_menu

    def get_all_search_results(self):
        all_search_results = self.find_elements(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_RESULT_LINKS, time=2)
        all_links = [x.get_attribute('href') for x in all_search_results]
        return all_links

    # Helper to google the exact keyword
    def google_word(self, word):
        self.go_to_site()
        self.enter_word(word)
        self.perform_search()
