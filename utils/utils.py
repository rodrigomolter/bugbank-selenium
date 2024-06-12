class Utils():
  
  def currency_to_float(text: str) -> float:
    text = text.replace("R$", "").strip()
    return float(text.replace(".", "").replace(",", "."))
  
  def format(text: str) -> str:
    return text.replace("\n", "").strip()
  