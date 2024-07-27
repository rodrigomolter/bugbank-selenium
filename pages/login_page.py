import json
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from utils.locators import LoginPageLocators
from models.customer import Customer

class LoginPage(BasePage):
  def __init__(self, webdriver: webdriver) -> None:
    self.locator = LoginPageLocators
    super().__init__(webdriver)

  def login_valid_credentials(self, email: str, password: str) -> None:
    self.find_element(self.locator.EMAIL).send_keys(email)
    self.find_element(self.locator.PASSWORD).send_keys(password)
    self.find_element(self.locator.BTN_SUBMIT).click()

  def get_alert(self) -> WebElement:
    self.wait_element(self.locator.MODAL_TEXT)
    return self.find_element(self.locator.MODAL_TEXT).get_attribute("innerText")
  
  def get_user_details(self, email: str) -> dict:
    response = self.webdriver.execute_script(f"return window.localStorage.getItem('{email}');")
    if response:
      return json.loads(response)
    return {}
    
  def is_auth(self, email: str) -> bool:
    return bool(self.get_user_details(email).get('logged', False))
  
  def auth_by_api(self) -> None:
    self.webdriver.add_cookie({
        'name': 'bugbank-auth',
        'value': 'true',
        'path': '/',
        'expires': 1
      })
