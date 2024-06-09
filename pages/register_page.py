from faker import Faker
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from utils.locators import RegisterPageLocators

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


  def register_by_api(self, email: str = None, password: str = None,  name: str = None, withBalance: bool = False) -> dict:
    faker = Faker()
    name = name or faker.name()
    email = email or faker.email()
    password = password or faker.password()
    account_number = f"{faker.random_number(digits=3)}-{faker.random_digit()}"
    balance = 5000 if withBalance else 0

    script = f"""
      localStorage.setItem('{email}', JSON.stringify({{
        "name": "{name}",
        "email": "{email}",
        "password": "{password}",
        "accountNumber": "{account_number}",
        "balance": {balance},
        "logged": false
    }}));
    """
    self.webdriver.execute_script(script)
    return {'name': name, 'email': email, 'password': password, 'accountNumber': account_number, 'balance': balance}

  def user_created_successfully(self) -> WebElement:
    self.wait_element(self.locator.MODAL_TEXT)
    return self.find_element(self.locator.MODAL_TEXT)
