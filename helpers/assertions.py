from conftest import driver_chrome
from helpers.base import BasePage


class Assertion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until = 10

    def assert_text_in_element(self, locator, expected_result):
        element = self.wait_for_visible(locator)
        assert element.text == expected_result, "Text not the same"

    def assert_value_in_element_attribute(self, locator, attribute,
                                          expected_result):
        element = self.wait_for_visible(locator)
        value = element.get_attribute(attribute)
        assert value == expected_result, f"Attribute {value} not the same"

    def assert_actual_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected URL: {expected_url}, " \
                                           f"Actual URL: {actual_url}"
