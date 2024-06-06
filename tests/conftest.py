"""
This module contains shared fixtures.
"""

import pytest
import selenium.webdriver


@pytest.fixture
def browser():

  b = selenium.webdriver.Chrome()
  b.implicitly_wait(10)
  yield b
  
  b.quit()