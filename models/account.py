from models.transfer import Transfer
from faker import Faker

class Account():
  def __init__(self, account_number: str = None, with_balance: bool = False) -> None:
    faker = Faker()
    self.account_number = account_number or f"{faker.random_number(digits=3)}-{faker.random_digit()}"
    self.transfers: list[Transfer] = []
    self.balance = 0
    description =  "Cliente optou por não ter saldo ao abrir conta" 
    if with_balance:
      self.balance = 1000
      description = "Saldo adicionado ao abrir conta"
      
    self.transfers.append(Transfer(type="Abertura de conta", description=description, transfer_value=self.balance))

  def balance(self) -> float:
    return self.balance
  
  def transfers(self) -> list[Transfer]:
    return self.transfers
  
  def new_transfer(self, transfer: Transfer) -> list[Transfer]:
    self.transfers.append(transfer)
    self.update_balance(transfer.transfer_value)
    return self.transfers
  
  def update_balance(self, transfer_amount: float) -> float:
    self.balance += transfer_amount
    return self.balance

    
