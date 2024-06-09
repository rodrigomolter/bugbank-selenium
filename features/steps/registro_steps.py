from behave import given, when, then
from pages.register_page import RegisterPage

@given('que eu estou na página de registro')
def open_register_page(context):
  context.page = RegisterPage(context.browser)
  context.page.open()


@when('eu preencho o formulário de cadastro')
def fill_register_form(context):
    for linha in context.table.rows:
      credentials = dict(linha.items())
    credentials["comSaldo"] = True if credentials['comSaldo'] == "sim" else False
    context.page.register_by_ui(name=credentials["nome"], email=credentials["email"], password=credentials["senha"], withBalance=credentials["comSaldo"])


@then('devo receber uma confirmação de que minha conta foi criada com sucesso')
def account_created_successfully(context):
  assert context.page.user_created_successfully()