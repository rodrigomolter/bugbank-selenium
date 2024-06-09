import datetime
import uuid

class Transfer():
  def __init__(self, type: str, description: str, transferValue: float) -> None:
    self.id = str(uuid.uuid4())
    self.date = datetime.datetime.now().strftime("%d/%m/%Y")
    self.type = type
    self.description = description
    self.transferValue = transferValue
