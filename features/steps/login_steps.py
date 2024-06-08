from behave import given, when, then
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from json import loads

@given('que eu esteja na página login')
def go_to_page(context):
  context.page = LoginPage (context.browser)
  context.page.open(context.base_url)


@when('efetuar login com dados validos')
def login_successfully(context):
  for linha in context.table.rows:
    credentials = dict(linha.items())
  RegisterPage(context.browser).register_by_api(email=credentials['email'], password=credentials['senha'])
  context.page.login_valid_credentials(credentials['email'], credentials['senha'])

@when('efetuar login com dados invalidos')
def login_successfully(context):
  for linha in context.table.rows:
    credentials = dict(linha.items())

  context.page.login_valid_credentials(credentials['email'], credentials['senha'])

@then('sou redirecionado para a Home')
def must_be_in_page(context):
  context.page = HomePage(context.browser)
  assert context.page.is_at_page() 

@then('recebo aviso de email ou senha invalido')
def user_or_password_invalid(context):
  assert context.page.have_invalid_user_alert()