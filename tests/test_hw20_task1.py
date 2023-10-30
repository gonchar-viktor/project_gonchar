import time

import pytest
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver_chrome
from pages.hw19_20_kfc_page import AuthorizationPage


class TestKFC:

    @pytest.fixture(scope='function')
    def authorization_kfc(self, driver_chrome):
        """
        Authorization fixture on the website KFC. Steps:
            1. Open a website 'https://www.kfc.by'
            2. Close the pop-up banner
            3. Click on the "personal profile" button
            4. Enter your username and password
            5. Click on the "log in" button
            6. Close the pop-up banner again
            7. Wait for an item available to an authorized user to load
        """

        authorization = AuthorizationPage(driver_chrome)
        authorization.open_page(authorization.link_main_page)
        authorization.hard_click(authorization.locator_profile)
        authorization.fill(
            authorization.locator_login, authorization.text_login)
        authorization.fill(
            authorization.locator_password, authorization.text_password)
        authorization.hard_click(authorization.locator_enter)

        assert EC.element_to_be_clickable(authorization.find_element_func(
                authorization.locator_profile_authorized_user))

    def test_visibility_and_clickability_of_buttons(self, driver_chrome,
                                                    authorization_kfc):
        """
        Precondition: the user must be logged in to the site
        'https://www.kfc.by' !
        Checking the display and clickability of buttons available on the page
        after user authorization
        """

        page = AuthorizationPage(driver_chrome)
        time.sleep(1)
        page.assert_elements_visibility_and_clickability(
            page.locator_basket, page.locator_orders, page.locator_favorites)

    def test_authorized_user(self, driver_chrome, authorization_kfc):
        """
        Precondition: the user must be logged in to the site
        'https://www.kfc.by' !
        Checking that the user is logged in to the site by viewing his
        user-name in the profile section.
        """

        page = AuthorizationPage(driver_chrome)
        page.hard_click(page.locator_profile_authorized_user)
        page.assert_text_in_element(
            page.locator_name_authorized_user, 'Виктор')

    def test_vk_icon(self, driver_chrome):
        """
        Checking that after clicking on the "vk" logo button, the desired page
        opened
        """

        page = AuthorizationPage(driver_chrome)
        page.open_page(page.link_main_page)
        page.hard_click(page.locator_reject_cookies)
        page.scroll_and_assert_scrollable_element_is_visible(
            page.locator_vk_icon)
        page.hard_click(page.locator_vk_icon)
        page.driver.switch_to.window(page.driver.window_handles[1])
        page.assert_actual_url(page.link_to_vk_expected)

    def test_address_display(self, driver_chrome, authorization_kfc):
        """
        Precondition: the user must be logged in to the site
        'https://www.kfc.by' !
        Checking that the entered text corresponds to the expected result
        """

        page = AuthorizationPage(driver_chrome)
        page.open_page(page.link_account)
        page.hard_click(page.locator_add_address_button)
        page.fill(page.locator_address_display, page.param_text)
        page.assert_value_in_element_attribute(
            page.locator_address_display, 'value', page.param_text)

    def test_profile_icon_selected(self, driver_chrome, authorization_kfc):
        """
        Precondition: the user must be logged in to the site
        'https://www.kfc.by' !
        Checking that when you click on the profile icon, it is selected
        """

        page = AuthorizationPage(driver_chrome)
        param = page.hard_click(page.locator_profile_authorized_user)
        assert EC.element_to_be_selected(param)
