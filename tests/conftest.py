"""
This module contains shared fixtures.
"""

import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):
  
  with open('config.json') as config_file:
    config = json.load(config_file) 
  
  assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome', 'Headless Firefox']
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0

  return config

@pytest.fixture
def browser(config):

  if config['browser'] == 'Firefox':
    b = selenium.webdriver.Firefox()
  elif config['browser'] == 'Chrome':
    b = selenium.webdriver.Chrome()
  elif config['browser'] == 'Headless Chrome':
    opts = selenium.webdriver.ChromeOptions()
    opts.add_argument('headless')
    b = selenium.webdriver.Chrome(options=opts)
  elif config['browser'] == 'Headless Firefox':
    opts = selenium.webdriver.FirefoxOptions()
    opts.add_argument('--headless')
    b = selenium.webdriver.Firefox(options=opts)
  else:
    raise Exception(f'Browser "{config["browser"]}" is not supported')

  b.implicitly_wait(config['implicit_wait'])
  yield b
 
  b.quit()