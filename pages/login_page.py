from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from utils.locators import LoginPageLocators

class LoginPage(BasePage):
  def __init__(self, webdriver: webdriver) -> None:
    self.locator = LoginPageLocators
    super().__init__(webdriver)

  def login_valid_credentials(self, email: str, password: str) -> None:
    self.find_element(self.locator.EMAIL).send_keys(email)
    self.find_element(self.locator.PASSWORD).send_keys(password)
    self.find_element(self.locator.BTN_SUBMIT).click()

  def have_invalid_user_alert(self) -> WebElement:
    self.wait_element(self.locator.MODAL_TEXT)
    return self.find_element(self.locator.MODAL_TEXT)