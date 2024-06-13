from behave import given, then, step

from pages.bank_statement_page import BankStatementPage
from pages.register_page import RegisterPage
from pages.transfer_page import TransferPage
from utils.utils import Utils

@given('que o usuário está na tela de extrato do BugBank')
def step_open_bank_statement_page(context):
  register_page = RegisterPage(context.browser)
  context.customer = register_page.create_user_and_authenticate(with_balance=True)
  context.target = register_page.register_by_api(with_balance=True)

  context.page = BankStatementPage(context.browser)
  context.page.open("/bank-statement")


@then('o sistema deve exibir o saldo disponível na conta do usuário')
def step_balance_must_be_visible(context):
  assert Utils.currency_to_float(context.page.get_balance()) == context.customer.account.balance

@step('possua criado uma conta com "Criar conta com saldo"')
def step_create_new_account(context):
  ...

@then('o sistema deve exibir a transação com a data da operação e o tipo de transação "{message}"')
def step_operation_date_and_operation_type_must_be_visible(context, message):
  assert any(type.text == message for type in context.page.get_transactions_type()), f"Nenhuma transação possui a mensagem esperada: {message}"
  assert [date != '' for date in context.page.get_transactions_date()], f"Pelo menos um campo data vazio!"

@step('tiver realizado uma transferência para outra conta anteriormente')
def step_sended_new_transaction(context):
  context.customer.account.transfers = TransferPage(context.browser).transaction_by_api(customer=context.customer, target=context.target)
  context.browser.refresh()

@step('tiver recebido uma transferência de outra conta anteriormente')
def step_received_new_transaction(context):
  context.target.account.transfers = TransferPage(context.browser).transaction_by_api(customer=context.target, target=context.customer)
  context.browser.refresh()

@then('o valor da transação deve estar em vermelho, indicando uma saída de fundos')
def step_transaction_must_be_red(context):
  assert context.page.get_transactions_value()[0].get_attribute("type") == "Abertura de conta"
  assert context.page.get_transactions_value()[1].get_attribute("type") == "withdrawal"

@then('o valor da transação deve estar em verde, indicando uma entrada de fundos')
def step_transaction_must_be_green(context):
  assert context.page.get_transactions_value()[0].get_attribute("type") == "Abertura de conta"
  assert context.page.get_transactions_value()[1].get_attribute("type") == "input"

@step('tiver realizado uma transação sem descrição')
def step_transaction_with_no_description(context):
  context.target.account.transfers = TransferPage(context.browser).transaction_by_api(customer=context.customer, target=context.target, description='')
  context.browser.refresh()

@then('possuir a descrição "{description}"')
def step_must_contain_no_description(context, description):
  assert context.page.get_transactions_description()[1].text == description, f"Descrição esperada ({description}) difere da descrição obtida ({context.page.get_transactions_description()[1].text})"