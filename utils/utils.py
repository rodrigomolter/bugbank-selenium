import configparser
import re

config = configparser.ConfigParser()
CONFIG_FILE = 'behave.ini'

class Utils():
  
  def currency_to_float(text: str) -> float:
    text = text.replace("R$", "").strip()
    return float(text.replace(".", "").replace(",", "."))
  
  def format(text: str) -> str:
    return text.replace("\n", "").strip()
  
  def get_app_url() -> str:
    config.read(CONFIG_FILE)
    return config.get('behave.userdata', 'base_url')
  
  def has_account_number(text: str) -> bool:
    return re.search(r'\d{2,3}-\d', text) != None
