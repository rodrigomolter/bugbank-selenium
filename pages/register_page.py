from faker import Faker
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from utils.locators import RegisterPageLocators
from models.customer import Customer

class RegisterPage(BasePage):

  def __init__(self, webdriver: webdriver) -> None:
    self.locator = RegisterPageLocators
    super().__init__(webdriver)


  def open(self, path: str = '') -> None:
    self.webdriver.get(str(self.base_url + path))
    self.find_element(self.locator.BTN_REGISTER).click()


  def register_by_ui(self, email: str = None, password: str = None, name: str = None, withBalance: bool = False) -> None:
    faker = Faker()
    name = name or faker.name()
    email = email or faker.email()
    password = password or faker.password()

    self.find_element(self.locator.EMAIL).send_keys(email)
    self.find_element(self.locator.NAME).send_keys(name)
    self.find_element(self.locator.PASSWORD).send_keys(password)
    self.find_element(self.locator.PASSWORD_CONFIRMATION).send_keys(password)
    if withBalance:
      self.find_element(self.locator.ADD_BALANCE).click()

    self.find_element(self.locator.BTN_SUBMIT).click()


  def register_by_api(self, email: str = None, password: str = None,  name: str = None, withBalance: bool = False) -> Customer:
    customer = Customer(email=email, name=name, password=password, withBalance=withBalance)

    script = f"""
      localStorage.setItem('{customer.email}', JSON.stringify({{
        "name": "{customer.name}",
        "email": "{customer.email}",
        "password": "{customer.password}",
        "accountNumber": "{customer.account.accountNumber}",
        "balance": {customer.account.balance},
        "logged": false
    }}));
    """
    self.webdriver.execute_script(script)
    return customer

  def user_created_successfully(self) -> WebElement:
    self.wait_element(self.locator.MODAL_TEXT)
    return self.find_element(self.locator.MODAL_TEXT)
