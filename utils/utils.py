class Utils():
  
  def currency_to_float(self, text: str) -> float:
    return float(text.replace(".", "").replace(",", "."))
  