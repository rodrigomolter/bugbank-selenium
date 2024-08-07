from abc import ABC
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.utils import Utils

class BasePage(ABC):
  def __init__(self, webdriver: webdriver) -> None:
    self.webdriver: webdriver = webdriver
    self.base_url = Utils.get_app_url()

  def find_element(self, locator: tuple[By, str]) -> WebElement:
    self.wait_element(locator)
    return self.webdriver.find_element(*locator)

  def find_elements(self, locator: tuple[By, str]) -> list[WebElement]:
    self.wait_element(locator)
    return self.webdriver.find_elements(*locator)
  
  def open(self, path: str = '') -> None:
    self.webdriver.get(str(self.base_url + path))

  def get_title(self) -> str:
    return self.webdriver.title
  
  def wait_element(self, locator: tuple[By, str]) -> None:
    try:
        WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))

  def is_visible(self, locator: tuple[By, str]) -> bool:
    try:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.is_displayed()
    except:
        return False
    
  def delete_browser_data(self) -> None:
    self.open()
    self.webdriver.execute_script("window.localStorage.clear();")
    self.webdriver.delete_all_cookies()
    self.webdriver.refresh()