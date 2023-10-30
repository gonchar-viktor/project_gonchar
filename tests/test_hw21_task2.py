from conftest import driver_chrome
from pages.hw21_demoqa_com_page import PracticeFormPage, DropdownListPage, \
    TextBoxPage, RadioButtonPage, DemoqaElementsPage


class TestDemoqaCom:

    def test_check_uncheck_checkbox(self, driver_chrome):  # 1
        """Check and uncheck the "Sports" element"""

        page = PracticeFormPage(driver_chrome)
        page.open_page(page.practice_form)
        page.double_click_checkbox_sports()
        page.assert_element_sport_is_not_selected()

    def test_scroll_page(self, driver_chrome):  # 2
        """Checking page scroll and element visibility"""

        page = TextBoxPage(driver_chrome)
        page.open_page(page.text_box)
        page.fill(page.locator_for_message, 'Looking down')
        page.scroll_and_assert_scrollable_element_is_visible(
            page.locator_element_interactions)

    def test_scroll_the_second_method(self, driver_chrome):  # 3
        """Checking the second method of page scrolling"""

        page = DemoqaElementsPage(driver_chrome)
        page.open_page(page.elements)
        page.scroll_func()
        assert True

    def test_radio_button(self, driver_chrome):  # 4
        """Checking if the desired element is selected"""

        page = RadioButtonPage(driver_chrome)
        page.open_page(page.radio_button)
        page.hard_click(page.locator_button_yes)
        page.hard_click(page.locator_button_impressive)
        page.hard_click(page.locator_button_yes)
        page.assert_is_the_desired_element_selected()

    def test_dropdown_list(self, driver_chrome):  # 5
        """Checking the drop-down list"""

        page = DropdownListPage(driver_chrome)
        page.open_page(page.select_menu)
        page.click_element(page.locator_select_title)
        page.click_element(page.locator_mr)
        page.assert_element_mr_selected()

    def test_get_text(self, driver_chrome):  # 6
        """
        Enter text in the input field, get from this text and compare with
        the expected
        """

        page = PracticeFormPage(driver_chrome)
        page.open_page(page.practice_form)
        text = 'Minsk'
        page.fill(page.locator_address, text)
        param1 = page.get_attribute_address("value")
        param2 = page.get_attribute_address("class")
        assert param1 == text and param2 == 'form-control'

    def test_existence_and_display_of_the_element(self, driver_chrome):  # 7
        """
        param1 : Checking what exists and is displayed on the page
        param2 : Checking what exists on the page
        """
        page = TextBoxPage(driver_chrome)
        page.open_page(page.text_box)
        param1 = page.find_element_func(page.locator_displayed)
        param2 = page.find_element_func(page.locator_present)
        page.assert_difference_of_methods(param1, param2)
