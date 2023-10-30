from pages.hw21_main_page import MainPage21HW
from selenium.webdriver.support import expected_conditions as EC


class PracticeFormPage(MainPage21HW):

    # for 1
    def assert_element_sport_is_not_selected(self):
        param = self.find_element_func(
            self.locator_checkbox_sports).is_selected()
        assert param is False

    def double_click_checkbox_sports(self):
        self.hard_click(self.locator_checkbox_sports)
        self.hard_click(self.locator_checkbox_sports)

    # for 6
    def get_attribute_address(self, val):
        return self.get_attribute_func(self.locator_address, val)


class TextBoxPage(MainPage21HW):

    def scroll_and_assert_scrollable_element_is_visible(self, val):
        """
        The function scrolls the page to the specified element and checks
        that it is visible on the page.
        :param val: scrollable element
        """
        element_interactions = self.wait_for_clicable(val)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", element_interactions)
        assert EC.visibility_of_element_located(val)

    @staticmethod
    def assert_difference_of_methods(val1, param2):
        param1 = val1.is_displayed()
        if EC.invisibility_of_element_located(param2):
            val2 = True
            assert (param1 and val2) is True


class DemoqaElementsPage(MainPage21HW):
    pass


class RadioButtonPage(MainPage21HW):
    def assert_is_the_desired_element_selected(self):
        """
        param_for_assert1: Checks that the element on the page is disabled
        param_for_assert2: Checks that the element on the page is selected
        """

        param_for_assert1 = self.find_element_func(
            self.locator_button_no).is_enabled()

        param_for_assert2 = self.find_element_func(
            self.locator_button_yes).is_selected()

        assert param_for_assert1 is False and param_for_assert2 is True


class DropdownListPage(MainPage21HW):
    def assert_element_mr_selected(self):
        param = self.find_element_func(self.locator_mr)
        assert EC.element_to_be_selected(param)
