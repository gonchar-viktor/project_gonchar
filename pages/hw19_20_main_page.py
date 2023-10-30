from elements.hw19_20_kfc_element import KFC
from helpers.assertions import Assertion
from helpers.fields import FieldsWebElement
from helpers.cookies import Cookies


class MainPage19HW20HW(Assertion, FieldsWebElement, Cookies, KFC):

    def open_page(self, link):
        self.driver.get(link)


