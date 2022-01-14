"""
This is a BASE page class that will be inherited by pages of the application under test
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import DEFAULT_WAITING_TIME, URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.message = "Can't find elements by locator \n"

    # Basic finder for the elements. Will wait for default amount of time until the element appears
    def find_element(self, locator, time=DEFAULT_WAITING_TIME):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"{self.message} {locator}")

    def find_elements(self, locator, time=DEFAULT_WAITING_TIME):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"{self.message} {locator}")

    def go_to_site(self, url=URL):
        return self.driver.get(url)

    def verify_title(self, url):
        self.driver.get(url)
        return self.driver.title
