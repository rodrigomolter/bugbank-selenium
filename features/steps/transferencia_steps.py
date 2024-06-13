from behave import given, when, then, step

from utils.utils import Utils
from pages.transfer_page import TransferPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.bank_statement_page import BankStatementPage
from models.transfer import Transfer

@given('que o usuário está na tela de transferência do BugBank')
def step_open_transfer_page(context):
  register_page = RegisterPage(context.browser)
  context.customer = register_page.create_user_and_authenticate()
  context.target = register_page.register_by_api()
  
  context.page = TransferPage(context.browser)
  context.page.open("/transfer")


@step('o saldo da conta do usuário é de "{saldo}"')
def step_define_user_balance(context, saldo):
  saldo = Utils.currency_to_float(saldo)
  context.customer.account.balance = saldo
  RegisterPage(context.browser).persist_user_info(context.customer, logged=True)

@when('o usuário preencher todos os campos corretamente')
def step_fill_transfer_form(context):
  context.transfer = Transfer()
  context.page.fill_transaction_form(account_number=context.target.account.account_number, transfer_value=context.transfer.transfer_value, description=context.transfer.description)

@when('tentar realizar a transferência')
def step_submit_transfer(context):
   context.page.click_to_transfer()

@then('o sistema deve debitar o valor transferido da conta do usuário')
def step_update_balance_with_transaction(context):
  updated_user_details = LoginPage(context.browser).get_user_details(context.customer.email)
  expected_balance = context.customer.account.balance - context.transfer.transfer_value
  context.customer.account.transfers = context.transfer
  assert updated_user_details["balance"] == expected_balance, f"Saldo atual ({updated_user_details['balance']}) diferente do saldo esperado ({expected_balance}))"

@then('o sistema deve redirecionar o usuário para a página de extrato')
def step_user_redirected_bank_statment_page(context):
  assert BankStatementPage(context.browser).is_at_page(), "Redirecionamento para a página Extrato não ocorreu"

@when('o usuário preencher o número da conta com um valor inválido ou inexistente')
def step_user_fill_wrong_account_number(context):
  invalid_account_number = "000-0"
  context.page.fill_account_number((invalid_account_number))
  context.page.fill_digit(invalid_account_number)

@when('o usuário preencher o valor da transferência com "{valor}"')
def step_custom_transfer_field(context, valor):
  context.page.fill_transfer_value(Utils.currency_to_float(valor))

@when('preencher os demais campos corretamente')
def step_fill_transfer_form_missing_fields(context):
  transfer = Transfer()

  if not context.page.get_transfer_value():
    context.page.fill_transfer_value(transfer.transfer_value)

  if not context.page.get_account_number():
   context.page.fill_account_number(context.target.account.account_number)

  if not context.page.get_digit():
   context.page.fill_digit(context.target.account.account_number)

  if not context.page.get_description():
   context.page.fill_description(transfer.description)

@then('a mensagem "{mensagem}" deve ser exibida')
def step_success_message(context, mensagem):
  alert = context.page.get_alert().get_attribute("innerText")
  assert Utils.format(alert) == mensagem, f'Mensagem "{mensagem}" não encontrada.'