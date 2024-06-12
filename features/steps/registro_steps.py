import re
from behave import given, when, then, step

from pages.register_page import RegisterPage
from models.customer import Customer
from pages.login_page import LoginPage
from utils.utils import Utils

@given('que o usuário está na tela de cadastro do BugBank')
def step_open_register_page(context):
  context.page = RegisterPage(context.browser)
  context.page.open()
  context.page.delete_browser_data()
  context.page.open()
  
@when('o usuário se cadastrar corretamente com os seguintes dados')
def step_register_with_given_data(context):
    for linha in context.table.rows:
      credentials = dict(linha.items())
    credentials["comSaldo"] = True if credentials['comSaldo'] == "sim" else False
    context.page.register_by_ui(name=credentials["nome"], email=credentials["email"], password=credentials["senha"], with_balance=credentials["comSaldo"])


@then('o sistema deve exibir receber uma mensagem de criação de conta com sucesso com o número da conta criada')
def step_account_created_successfully(context):
  text = context.page.get_alert().get_attribute("innerText")
  assert re.search(r'\d{2,3}-\d', text), f"O número da conta não foi encontrado no texto: {text}."

@when('o usuário tenta se cadastrar sem preencher o campo de {campo}')
def step_register_without_field(context, campo):

  FIELDS = {
   "nome" : "name",
   "email" : "email",
   "senha" : "password",
   "confirmar senha" : "password_confirmation"
   
  }
  context.page.register_without_field(FIELDS[campo])
  context.page.click_register_button()


@then('o sistema deve exibir a mensagem de campo obrigatório')
def step_missing_field_warning(context):
  assert context.page.mandatory_fields_warning(), f'Mensagem de campo obrigatório não encontrada.'

@then('o alerta de "{mensagem}" deve ser exibido')
def step_not_matching_password_alert(context, mensagem):
   alert = context.page.get_alert().get_attribute("innerText")
   assert Utils.format(alert) == mensagem, f'Mensagem "{mensagem}" não encontrada.'

@when('o usuário preencher o formulário de cadastro com o campo de senha com "{password}"')
def step_fill_register_form_custom_password(context, password):
    context.page.register_without_field(password)

@when('preencher o campo de confirmação de senha com "{password}"')
def step_fill_register_form_custom_confirmation_password(context, password):
   context.page.fill_password_confirmation(password)
   context.page.click_register_button()

@when('o usuário preencher todos os campos obrigatórios corretamente')
def step_fill_form(context):
   customer = Customer()
   context.customer = customer
   context.page.fill_form(email=customer.email, name=customer.name, password=customer.password)

@when('o usuário selecionar a opção "Criar conta com saldo"')
def step_add_balance(context):
   context.page.toggle_create_with_balance()
   context.page.click_register_button()

@when('o usuário não selecionar a opção "Criar conta com saldo"')
def step_not_add_balance(context):
  context.page.click_register_button()

@then('o sistema deve criar a conta com um saldo de "{value}"')
def step_new_account_with_balance(context, value):
  user = LoginPage(context.browser).get_user_details(context.customer.email)
  assert user.get("balance", False) == Utils.currency_to_float(value), f'Saldo atual ({user.get("balance", "Vazio")}) diferente do saldo esperado ({Utils.currency_to_float(value)})'
