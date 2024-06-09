from selenium.webdriver.common.by import By

class HomePageLocators():
  BTN_LOGOUT = (By.ID, "btnExit")

class LoginPageLocators():
  EMAIL = (By.CSS_SELECTOR, ".card__login input[name='email']")
  PASSWORD = (By.CSS_SELECTOR, ".card__login input[name='password']")
  BTN_SUBMIT = (By.XPATH, "//button[@type='submit'][contains(.,'Acessar')]")
  MODAL_TEXT = (By.ID, "modalText")
  BTN_CLOSE_MODAL = (By.ID, "btnCloseModal")

class RegisterPageLocators():
  EMAIL = (By.CSS_SELECTOR, ".card__register input[name='email']")
  NAME = (By.CSS_SELECTOR, ".card__register input[name='name']")
  PASSWORD = (By.CSS_SELECTOR, ".card__register input[name='password']")
  PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, ".card__register input[name='passwordConfirmation']")
  ADD_BALANCE = (By.ID, "toggleAddBalance")
  BTN_SUBMIT = (By.XPATH, "//button[@type='submit'][contains(.,'Cadastrar')]")
  BTN_REGISTER = (By.XPATH, "//div[@class='login__buttons']/button[text()='Registrar']")
  MODAL_TEXT = (By.ID, "modalText")