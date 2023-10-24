import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base import wait_for_clicable, hard_click, find_element_func, fill, \
    click_element
from conftest import driver_chrome, driver_firefox

# for 1
locator_checkbox_sports = By.ID, 'hobbies-checkbox-1'
# for 2
locator_for_message = By.ID, 'permanentAddress'
locator_element_interactions = By.XPATH, \
    '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[5]'
# for 4
locator_button_yes = By.ID, 'yesRadio'
locator_button_impressive = By.ID, 'impressiveRadio'
locator_button_no = By.ID, 'noRadio'
# for 5
locator_select_title = By.XPATH, '//div[text()="Select Title"]'
locator_mr = By.XPATH, '//*[text()="Mr."]'
# for 6
locator_address = By.CSS_SELECTOR, '[id="currentAddress"]'
# for 7
locator_present = By.CSS_SELECTOR, '[id="Ad.Plus-300x250"]'
locator_displayed = By.CSS_SELECTOR, '[id="Ad.Plus-300x250"]'


class TestDemoqaCom:

    def test_check_uncheck_checkbox(self, driver_chrome):  # 1
        """I set and uncheck the "Sports" element"""

        driver_chrome.get('https://demoqa.com/automation-practice-form')
        hard_click(driver_chrome, locator_checkbox_sports)
        hard_click(driver_chrome, locator_checkbox_sports)
        param = find_element_func(
            driver_chrome, locator_checkbox_sports).is_selected()

        assert param is False

    def test_scroll_page(self, driver_chrome):  # 2
        """Checking page scroll and element visibility"""

        driver_chrome.get('https://demoqa.com/text-box')
        fill(driver_chrome, locator_for_message, 'Looking down')
        element_interactions = wait_for_clicable(
            driver_chrome, locator_element_interactions)
        driver_chrome.execute_script(
            "arguments[0].scrollIntoView();", element_interactions)

        assert EC.visibility_of_element_located(element_interactions)

    def test_scroll_the_second_method(self, driver_chrome):  # 3
        """Checking the second method of page scrolling"""

        driver_chrome.get("https://demoqa.com/elements")
        scroll_height = 1000

        while True:
            driver_chrome.execute_script(
                f"window.scrollTo(0, {scroll_height});")
            time.sleep(2)  # for visibility
            scroll_height += 1000

            if scroll_height >= driver_chrome.execute_script(
                    "return document.body.scrollHeight;"):
                break

        assert True

    def test_radio_button(self, driver_chrome):  # 4
        """
        :param param_for_assert1: Checks that the element on the page
        is disabled
        :param param_for_assert2: Checks that the element on the page is
        selected
        """

        driver_chrome.get('https://demoqa.com/radio-button')

        button_yes = hard_click(driver_chrome, locator_button_yes)
        button_impressive = hard_click(
            driver_chrome, locator_button_impressive)
        button_yes = hard_click(driver_chrome, locator_button_yes)

        param_for_assert1 = find_element_func(
            driver_chrome, locator_button_no).is_enabled()
        param_for_assert2 = find_element_func(
            driver_chrome, locator_button_yes).is_selected()

        assert param_for_assert1 is False and param_for_assert2 is True

    def test_dropdown(self, driver_chrome):  # 5
        """Checking the drop-down list"""

        driver_chrome.get('https://demoqa.com/select-menu')

        click_element(driver_chrome, locator_select_title)
        click_element(driver_chrome, locator_mr)
        param = find_element_func(driver_chrome, locator_mr)

        assert EC.visibility_of_element_located(param)

    def test_get_text(self, driver_chrome):  # 6
        """
        Enter text in the input field, get from this text and compare with
        the expected
        """

        driver_chrome.get('https://demoqa.com/automation-practice-form')
        text = 'Minsk'
        address = wait_for_clicable(driver_chrome, locator_address)
        address.send_keys(text)

        param1 = address.get_attribute("value")
        param2 = address.get_attribute("class")
        print('\t', param2)

        assert param1 == text and param2 == 'form-control'

    def test_existence_and_display_of_the_element(self, driver_chrome):  # 7
        """
        :param1 : Checking what exists and is displayed on the page
        :param2 : Checking what exists on the page
        """
        driver_chrome.get('https://demoqa.com/text-box')
        param1 = find_element_func(driver_chrome, locator_displayed)
        param2 = find_element_func(driver_chrome, locator_present)
        val1 = param1.is_displayed()
        if EC.invisibility_of_element_located(param2):
            val2 = True

            assert (val1 and val2) is True
