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
  MODAL_TEXT = (By.XPATH, "//p[@id='modalText']")
  INPUT_WARNING = (By.CLASS_NAME, "input__warging")

class TransferPageLocators():
  ACCOUNT_NUMBER = (By.NAME, "accountNumber")
  DIGIT = (By.NAME, "digit")
  TRANSFER_VALUE = (By.NAME, "transferValue")
  DESCRIPTION = (By.NAME, "description")
  BTN_SUBMIT = (By.XPATH, "//form/button[@type='submit'][contains(.,'Transferir agora')]")
  MODAL_TEXT = (By.XPATH, "//p[@id='modalText']")

class BankStatementLocators():
  BALANCE = (By.ID, "textBalanceAvailable")
  TRANSFER_DESCRIPTION = (By.ID, "textDescription")
  TRANSFER_VALUE = (By.ID, "textTransferValue")
  TRANSFER_DATE = (By.ID, "textDateTransaction")
  TRANSFER_TYPE = (By.ID, "textTypeTransaction")
  TRANSFERS_CONTAINER = (By.XPATH, r"//*[contains(@class, 'bank-statement__Transaction')]")