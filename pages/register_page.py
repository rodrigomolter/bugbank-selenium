from faker import Faker
from selenium.webdriver.common.by import By
from page_objects.page_objects import Page

class RegisterPage(Page):
  email = (By.NAME, "email")
  name = (By.NAME, "name")
  password = (By.NAME, "password")
  passwordConfirmation = (By.NAME, "passwordConfirmation")
  addBalance = (By.ID, "toggleAddBalance")
  submit = (By.XPATH, "//button[@type='submit'][contains(.,'Cadastrar')]")
              

  fake = Faker()

  def register_by_ui(self, name, email, password, withBalance = False):
    name = name or self.fake.name()
    email = email or self.fake.email()
    password = password or self.fake.password()

    self.find_element(self.email).send_keys(email)
    self.find_element(self.name).send_keys(name)
    self.find_element(self.password).send_keys(password)
    self.find_element(self.passwordConfirmation).send_keys(password)
    self.find_element(self.passwordConfirmation).send_keys(password) if withBalance else None

    self.find_element(self.submit).click()


  def register_by_api(self, name='', email='', password='', withBalance = False):
    name = name or self.fake.name()
    email = email or self.fake.email()
    password = password or self.fake.password()
    account_number = f"{self.fake.random_number(digits=3)}-{self.fake.random_digit()}"
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