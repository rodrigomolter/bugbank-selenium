import datetime
import uuid
from faker import Faker

class Transfer():
  def __init__(self, description: str = None, transfer_value: float = None, type: str = "Input") -> None:

    faker = Faker()
    self.id = str(uuid.uuid4())
    self.date = datetime.datetime.now().strftime("%d/%m/%Y")
    self.type = type
    self.description = description or faker.catch_phrase()
    self.transfer_value = transfer_value or faker.random_int(min=1, max=500)
