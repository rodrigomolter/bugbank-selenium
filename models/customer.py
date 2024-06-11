from models.account import Account
from faker import Faker


class Customer():
  def __init__(self, name: str = None, email: str = None, password: str = None, with_balance: bool = False) -> None:
    faker = Faker()
    self.name = name or faker.name()
    self.email = email or faker.email()
    self.password = password or faker.password()

    self.account = Account(with_balance=with_balance)

