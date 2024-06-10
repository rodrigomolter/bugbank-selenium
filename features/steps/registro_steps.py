from behave import given, when, then
from pages.register_page import RegisterPage
import re

@given('que o usuário está na tela de cadastro do BugBank')
def open_register_page(context):
  context.page = RegisterPage(context.browser)
  context.page.open()

@when('o usuário se cadastra preenchendo todos os campos corretamente')
def fill_register_form(context):
    for linha in context.table.rows:
      credentials = dict(linha.items())
    credentials["comSaldo"] = True if credentials['comSaldo'] == "sim" else False
    context.page.register_by_ui(name=credentials["nome"], email=credentials["email"], password=credentials["senha"], withBalance=credentials["comSaldo"])


@then('devo receber uma mensagem de criação de conta com sucesso com o número da conta criada')
def account_created_successfully(context):
  assert re.search(r'\d{2,3}-\d', context.page.user_created_successfully().text), "O número da conta não foi encontrado no texto."