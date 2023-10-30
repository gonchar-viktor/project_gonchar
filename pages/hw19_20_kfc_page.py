from pages.hw19_20_main_page import MainPage19HW20HW
from selenium.webdriver.support import expected_conditions as EC


class AuthorizationPage(MainPage19HW20HW):

    def assert_elements_visibility_and_clickability(self, val1, val2, val3):
        param1 = self.find_element_func(val1)
        param2 = self.find_element_func(val2)
        param3 = self.find_element_func(val3)
        assert EC.visibility_of_element_located(
            param1 and param2 and param3) and EC.element_to_be_clickable(
            param1 and param2 and param3)






