from models.transfer import Transfer
from faker import Faker

class Account():
  def __init__(self, accountNumber: str = None, withBalance: bool = False) -> None:
    faker = Faker()
    self.accountNumber = accountNumber or f"{faker.random_number(digits=3)}-{faker.random_digit()}"
    self.transfers: list[Transfer] = []
    self.balance = 1000 if withBalance else 0
    self.transfers.append(Transfer(type="Abertura de conta", description="Saldo adicionado ao abrir conta", transferValue=self.balance))

    @property
    def balance(self) -> None:
      return self.balance
    
    @property
    def transfers(self) -> list[Transfer]:
      return self.transfers
    
    @transfers.setter
    def newTransfer(self, transfer: Transfer) -> list[Transfer]:
      self.transfer.append(transfer)
      self.updateBalance(transfer.transferValue)
      return self.transfers
    
    def updateBalance(self, transferAmount: int) -> int:
      self.balance += transferAmount
      return balance

    
