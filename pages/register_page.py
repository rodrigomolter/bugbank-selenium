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

  def fill_email(self, email: str) -> None:
    self.find_element(self.locator.EMAIL).send_keys(email)

  def fill_name(self, name: str) -> None:
    self.find_element(self.locator.NAME).send_keys(name)

  def fill_password(self, password: str) -> None:
    self.find_element(self.locator.PASSWORD).send_keys(password)

  def fill_password_confirmation(self, password: str) -> None:
    self.find_element(self.locator.PASSWORD_CONFIRMATION).send_keys(password)

  def toggle_create_with_balance(self) -> None:
    self.find_element(self.locator.ADD_BALANCE).click()

  def click_register_button(self) -> None:
      self.find_element(self.locator.BTN_SUBMIT).click()

  def fill_form(self, name: str, email: str, password: str) -> None:
    self.fill_email(email)
    self.fill_name(name)
    self.fill_password(password)
    self.fill_password_confirmation(password)


  def register_by_ui(self, email: str = None, password: str = None, name: str = None, withBalance: bool = False) -> None:
    customer = Customer(email=email, name=name, password=password, withBalance=withBalance)

    self.fill_form(customer.name, customer.email, customer.password)
    if withBalance:
      self.toggle_create_with_balance()
    self.click_register_button()


  def register_by_api(self, email: str = None, password: str = None,  name: str = None, withBalance: bool = False) -> Customer:
    customer = Customer(email=email, name=name, password=password, withBalance=withBalance)

    script = f"""
      localStorage.setItem("{customer.email}", JSON.stringify({{
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
  
  
  def register_without_field(self, field: tuple[str, str]) -> None:
    faker = Faker()

    password = faker.password()
    field_values = {
      "email" : faker.email(),
      "name" : faker.name(),
      "password" : password,
      "password_confirmation" : password
    }

    field_methods = {
        'email': self.fill_email,
        'name': self.fill_name,
        'password': self.fill_password,
        'password_confirmation': self.fill_password_confirmation
    }

    for key, method in field_methods.items():
        if field != key:
            method(field_values[key])



  def mandatory_fields_warning(self) -> list:
    if self.is_visible(self.locator.INPUT_WARNING):
      return self.find_elements(self.locator.INPUT_WARNING)
    return []
  
  def user_created_successfully(self) -> WebElement:
    self.wait_element(self.locator.MODAL_TEXT)
    return self.find_element(self.locator.MODAL_TEXT)