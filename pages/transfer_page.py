import json
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
import pages.register_page as rp
from models.transfer import Transfer
from models.customer import Customer
from utils.locators import TransferPageLocators

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
    return self.find_element(self.locator.MODAL_TEXT).get_attribute("innerText")
  
  def transaction_by_api(self, customer: Customer, target: Customer, transfer_value: float = None, description: str = None) -> Transfer:

    transfer = Transfer(account_number=customer.account.account_number,transfer_value=transfer_value,description=description)
    self.persist_transfer(target, transfer)
    target.account.new_transfer(transfer)

    transfer.type = "withdrawal"
    transfer.transfer_value = transfer.transfer_value * -1
    self.persist_transfer(customer, transfer)
    customer.account.new_transfer(transfer)

    register_page = rp.RegisterPage(self.webdriver)
    register_page.persist_user_info(customer)
    register_page.persist_user_info(target)
        
    return transfer
  
  
  def persist_transfer(self, customer: Customer, transfer: Transfer) -> None:
    response = self.webdriver.execute_script(f"return window.localStorage.getItem('transaction:{customer.email}');")
    transactions = []
    if response:
      transactions = json.loads(response)

    transactions.append({
       "date": transfer.date,
       "description": transfer.description,
       "id": transfer.id,
       "transferValue": transfer.transfer_value,
       "type": transfer.type
      })
    formated_json = json.dumps(transactions).replace('"', '\\"')
    script = f"""
      localStorage.setItem("transaction:{customer.email}", "{formated_json}");
    """
    self.webdriver.execute_script(script)