from selenium.webdriver.common.by import By
from page_objects.page_objects import Page

class LoginPage(Page):
  email = (By.NAME, "email")
  password = (By.NAME, "password")
  submit = (By.XPATH, "//button[@type='submit'][contains(.,'Acessar')]")

  modal_text = (By.ID, "modalText")
  close_modal = (By.ID, "btnCloseModal")

  def login_valid_credentials(self, email=email, password=password):
    self.find_element(self.email).send_keys(email)
    self.find_element(self.password).send_keys(password)
    self.find_element(self.submit).click()


  def have_invalid_user_alert(self):
    return self.find_element(self.modal_text)