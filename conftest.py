"""
THis is a fixture to execute SetUp function for running the tests. E.g. initialize webdriver before using it
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def browser():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()

