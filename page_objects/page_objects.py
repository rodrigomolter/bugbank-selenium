from abc import ABC


class SeleniumObject:
    def find_element(self, locator):
        return self.webdriver.find_element(*locator)

    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)


class Page(ABC, SeleniumObject):
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.url = ''
        self._reflection()

    def open(self, url):
        self.url = url
        self.webdriver.get(url)

    def _reflection(self):
        for atributo in dir(self):
            atributo_real = getattr(self, atributo)
            if isinstance(atributo_real,PageElement):
                atributo_real.webdriver = self.webdriver


class PageElement(ABC, SeleniumObject):
    def __init__(self, webdriver=None):
        self.webdriver = webdriver