from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from utils.locators import BankStatementLocators

class BankStatementPage(BasePage):

  def __init__(self, webdriver: webdriver) -> None:
    self.locator = BankStatementLocators
    super().__init__(webdriver)

  def is_at_page(self) -> WebElement:
    self.wait_element(self.locator.BALANCE)
    return self.find_element(self.locator.BALANCE)
  
  def get_balance(self) -> str:
    self.wait_element(self.locator.BALANCE)
    return self.find_element(self.locator.BALANCE).text
  
  def get_transactions_type(self) -> list[WebElement]:
    self.wait_element(self.locator.TRANSFER_TYPE)
    return self.find_elements(self.locator.TRANSFER_TYPE)

  def get_transactions_date(self) -> list[WebElement]:
    self.wait_element(self.locator.TRANSFER_DATE)
    return self.find_elements(self.locator.TRANSFER_DATE)

  def get_transactions_description(self) -> list[WebElement]:
    self.wait_element(self.locator.TRANSFER_DESCRIPTION)
    return self.find_elements(self.locator.TRANSFER_DESCRIPTION)
  
  def get_transactions_value(self) -> list[WebElement]:
    self.wait_element(self.locator.TRANSFER_VALUE)
    return self.find_elements(self.locator.TRANSFER_VALUE)