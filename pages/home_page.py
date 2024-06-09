from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from utils.locators import HomePageLocators

class HomePage(BasePage):
  def __init__(self, webdriver: webdriver) -> None:
    self.locator = HomePageLocators
    super().__init__(webdriver)

  def is_at_page(self) -> WebElement:
    self.wait_element(self.locator.BTN_LOGOUT)
    return self.find_element(self.locator.BTN_LOGOUT)