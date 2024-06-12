from behave import given, when, then
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.register_page import RegisterPage

@given('que o usuário está na página de login do BugBank')
def open_login_page(context):
  context.page = LoginPage (context.browser)
  context.page.open()
  context.page.delete_browser_data()

@when('o usuário fazer login com o email "{email}" e senha "{password}"')
def login_successfully(context, email, password):
  context.email = email
  RegisterPage(context.browser).register_by_api(email=email, password=password)
  context.page.login_valid_credentials(email, password)

@then('o usuário deve ser autenticado com sucesso')
def auth_successfully(context):
  assert context.page.is_auth(context.email)

@then('o sistema deve redirecionar o usuário para a página inicial')
def must_be_in_page(context):
  context.page = HomePage(context.browser)
  assert context.page.is_at_page(), "Pagina atual não é a página inicial"

@when('o usuário tentar fazer login com o email "{email}" e senha "{password}" não cadastrados')
def login_unsuccessfully(context, email, password):
  context.email = email
  context.page.login_valid_credentials(email, password)

@then('o sistema deve exibir uma mensagem informando "{mensagem}"')
def user_or_password_invalid(context, mensagem):
  text = context.page.get_alert().get_attribute("innerText")
  assert text.split("\n")[0] == mensagem, f'Mensagem "{mensagem}" não encontrada.'

@then('o usuário não deve ser autenticado')
def auth_not_successfully(context):
  assert not context.page.is_auth(context.email), "Usuário autenticado!"