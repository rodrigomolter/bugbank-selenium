from selenium.webdriver.common.by import By
from page_objects.page_objects import Page

class HomePage(Page):
  accountNumber = (By.ID, "textAccountNumber")


  def is_at_page(self):
    return self.webdriver.find_element(*self.accountNumber)