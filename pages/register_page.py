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


  def register_by_ui(self, email: str = None, password: str = None, name: str = None, with_balance: bool = False) -> None:
    customer = Customer(email=email, name=name, password=password, with_balance=with_balance)

    self.fill_form(customer.name, customer.email, customer.password)
    if with_balance:
      self.toggle_create_with_balance()
    self.click_register_button()


  def register_by_api(self, email: str = None, password: str = None,  name: str = None, with_balance: bool = False, logged: bool = False) -> Customer:
    customer = Customer(email=email, name=name, password=password, with_balance=with_balance)

    script = f"""
      localStorage.setItem("{customer.email}", JSON.stringify({{
        "name": "{customer.name}",
        "email": "{customer.email}",
        "password": "{customer.password}",
        "accountNumber": "{customer.account.account_number}",
        "balance": {customer.account.balance},
        "logged": {str(logged).lower()}
    }}));
    """
    self.webdriver.execute_script(script)
    return customer
  
  def persist_user_info(self, customer: Customer, logged: bool = False) -> None:

    script = f"""
      localStorage.setItem("{customer.email}", JSON.stringify({{
        "name": "{customer.name}",
        "email": "{customer.email}",
        "password": "{customer.password}",
        "accountNumber": "{customer.account.account_number}",
        "balance": {customer.account.balance},
        "logged": {str(logged).lower()}
    }}));
    """
    self.webdriver.execute_script(script)
  
  
  def register_without_field(self, field: tuple[str, str]) -> None:
    customer = Customer()

    field_values = {
      "email" : customer.email,
      "name" : customer.name,
      "password" : customer.password,
      "password_confirmation" : customer.password
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

  def mandatory_fields_warning(self) -> bool:
    return any(element.is_displayed() for element in self.find_elements(self.locator.INPUT_WARNING))

  
  def get_alert(self) -> WebElement:
    self.wait_element(self.locator.MODAL_TEXT)
    return self.find_element(self.locator.MODAL_TEXT)