import re
from faker import Faker
from behave import given, when, then

from pages.register_page import RegisterPage
from models.customer import Customer
from pages.login_page import LoginPage

@given('que o usuário está na tela de cadastro do BugBank')
def step_open_register_page(context):
  context.page = RegisterPage(context.browser)
  context.page.open()

@when('o usuário se cadastrar corretamente com os seguintes dados')
def step_register_with_given_data(context):
    for linha in context.table.rows:
      credentials = dict(linha.items())
    credentials["comSaldo"] = True if credentials['comSaldo'] == "sim" else False
    context.page.register_by_ui(name=credentials["nome"], email=credentials["email"], password=credentials["senha"], withBalance=credentials["comSaldo"])


@then('o sistema deve exibir receber uma mensagem de criação de conta com sucesso com o número da conta criada')
def step_account_created_successfully(context):
  text = context.page.user_created_successfully().get_attribute("innerText")
  assert re.search(r'\d{3}-\d', text), f"O número da conta não foi encontrado no texto: {text}."

@when('o usuário tenta se cadastrar sem preencher o campo de {campo}')
def step_register_without_field(context, campo):

  FIELDS = {
   "nome" : "name",
   "email" : "email",
   "senha" : "password",
   "confirmar senha" : "password_confirmation"
   
  }
  context.page.register_without_field(FIELDS[campo])


@then('o sistema deve exibir a mensagem de {mensagem}')
def step_missing_field_warning(context, mensagem):
   True
   # TODO
  # assert len(context.page.mandatory_fields_warning()) > 0

@when('o usuário preencher o formulário de cadastro com o campo de senha com "{password}"')
def step_fill_register_form_custom_password(context, password):
    context.page.register_without_field("password")

@when('preencher o campo de confirmação de senha com "{password}"')
def step_fill_register_form_custom_confirmation_password(context, password):
   context.page.fill_password_confirmation(password)

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

@then('o sistema deve criar a conta com um saldo de R$ {value}')
def step_new_account_with_balance(context, value):
  user = LoginPage(context.browser).get_user_details(context.customer.email)
  expected_balance = float(value.replace(".", "").replace(",", "."))
  assert user.get("balance", False) == expected_balance
