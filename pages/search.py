"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:

  # URL

  URL = 'https://www.duckduckgo.com'

  # Locators

  SEARCH_INPUT = (By.ID, 'searchbox_input')
  SEARCH_BUTTON = (By.CLASS_NAME, 'searchbox_iconWrapper__suWUe')
  MORE_RESULT = (By.ID, 'rld-1')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def search(self, phrase):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.send_keys(phrase)

    search_button = self.browser.find_element(*self.SEARCH_BUTTON)
    search_button.click()

    more_result = self.browser.find_element(*self.MORE_RESULT)
    more_result.click()

