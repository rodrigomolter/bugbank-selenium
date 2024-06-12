from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from utils.locators import BankStatementLocators
from models.customer import Customer

class BankStatementPage(BasePage):

  def __init__(self, webdriver: webdriver) -> None:
    super().__init__(webdriver)
    self.locator = BankStatementLocators

  def is_at_page(self):
    self.wait_element(self.locator.BALANCE)
    return self.find_element(self.locator.BALANCE)
