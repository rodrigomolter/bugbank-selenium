from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from utils.locators import TransferPageLocators
from models.customer import Customer

class TransferPage(BasePage):

  def __init__(self, webdriver: webdriver) -> None:
    self.locator = TransferPageLocators
    super().__init__(webdriver)


  def fill_account_number(self, account_number: str) -> None:
    self.find_element(self.locator.ACCOUNT_NUMBER).send_keys(account_number[:-2])

  def fill_digit(self, account_number: str) -> None:
    self.find_element(self.locator.DIGIT).send_keys(account_number[-1])

  def fill_transfer_value(self, value: float) -> None:
    self.find_element(self.locator.TRANSFER_VALUE).send_keys(value)

  def fill_description(self, description: str) -> None:
    self.find_element(self.locator.DESCRIPTION).send_keys(description)

  def click_to_transfer(self) -> None:
    self.find_element(self.locator.BTN_SUBMIT).click()

  def get_account_number(self):
      return self.find_element(self.locator.ACCOUNT_NUMBER).get_attribute('value')

  def get_digit(self):
      return self.find_element(self.locator.DIGIT).get_attribute('value')

  def get_transfer_value(self):
      return self.find_element(self.locator.TRANSFER_VALUE).get_attribute('value')

  def get_description(self):
      return self.find_element(self.locator.DESCRIPTION).get_attribute('value')

  def fill_transaction_form(self, account_number: str, transfer_value: float, description: str) -> None:
    self.fill_account_number(account_number)
    self.fill_digit(account_number)
    self.fill_transfer_value(transfer_value)
    self.fill_description(description)    

  def make_new_transaction(self, account_number: str, transfer_value: float, description: str) -> None:
    self.fill_transaction_form(account_number, transfer_value, description)
    self.click_to_transfer()

  def get_alert(self) -> WebElement:
    self.wait_element(self.locator.MODAL_TEXT)  
    return self.find_element(self.locator.MODAL_TEXT)