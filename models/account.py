from models.transfer import Transfer
from faker import Faker

class Account():
  def __init__(self, account_number: str = None, with_balance: bool = False) -> None:
    faker = Faker()
    self.account_number = account_number or f"{faker.random_number(digits=3)}-{faker.random_digit()}"
    self.transfers: list[Transfer] = []
    self.balance = 1000 if with_balance else 0
    self.transfers.append(Transfer(type="Abertura de conta", description="Saldo adicionado ao abrir conta", transfer_value=self.balance))

    @property
    def balance(self) -> float:
      return self.balance
    
    @property
    def transfers(self) -> list[Transfer]:
      return self.transfers
    
    @transfers.setter
    def new_transfer(self, transfer: Transfer) -> list[Transfer]:
      self.transfer.append(transfer)
      self.updateBalance(transfer.transfer_value)
      return self.transfers
    
    def update_balance(self, transfer_amount: float) -> float:
      self.balance += transfer_amount
      return balance

    
