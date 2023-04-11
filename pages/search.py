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
  SUGGESTION_LIST = (By.XPATH, '//li[@class="searchbox_suggestion__csrUQ"]')


  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def search(self, phrase, suggestion):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.send_keys(phrase)

    suggestions_list = self.browser.find_elements(*self.SUGGESTION_LIST)
    suggestions_list[suggestion].click()


