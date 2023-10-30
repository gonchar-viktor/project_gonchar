from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

from conftest import driver_chrome


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_until = 10

    def wait_for_clicable(self, locator):
        """
        Waiting until the element becomes clickable otherwise an error will
        be caused
        """
        try:
            return WebDriverWait(self.driver, self.wait_until).until(
                EC.element_to_be_clickable(locator))
        except WebDriverException:
            assert False, f"Element {locator} not clicable"

    def wait_for_visible(self, locator):
        """
        Waiting until the element becomes visible, otherwise an error will be
        caused
        """
        try:
            return WebDriverWait(self.driver, self.wait_until).until(
                EC.visibility_of_element_located(locator))
        except WebDriverException:
            assert False, f"Element {locator} not displayed"

    def find_element_func(self, locator):
        self.driver.implicitly_wait(self.wait_until)
        element = self.driver.find_element(*locator)
        return element

    def hard_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def click_element(self, locator):
        self.driver.implicitly_wait(self.wait_until)
        self.driver.find_element(*locator).click()

    def click_on(self, locator):
        element = self.wait_for_visible(locator)
        element.click()

    def get_current_url(self):
        return self.driver.current_url

    def get_attribute_func(self, locator, text):
        return self.driver.find_element(*locator).get_attribute(text)

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

    def scroll_func(self):
        """The function scrolls the page to the end"""
        scroll_height = 1000
        while True:
            self.driver.execute_script(
                f"window.scrollTo(0, {scroll_height});")
            scroll_height += 1000

            if scroll_height >= self.driver.execute_script(
                    "return document.body.scrollHeight;"):
                break
