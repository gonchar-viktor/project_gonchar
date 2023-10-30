from elements.hw21_demoqa_com_element import DemoqaCom
from helpers.assertions import Assertion
from helpers.fields import FieldsWebElement
from helpers.cookies import Cookies
from elements.hw21_bbc_com_element import BBC


class MainPage21HW(Assertion, FieldsWebElement, Cookies, DemoqaCom, BBC):

    def open_page(self, link):
        self.driver.get(link)
