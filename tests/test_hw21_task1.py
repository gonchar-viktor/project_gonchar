import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.hw21_bbc_com_page import BBCNewsPage
from conftest import driver_chrome


class TestBBC:

    @pytest.fixture(scope='function')
    def bbs_website(self, driver_chrome):
        page = BBCNewsPage(driver_chrome)
        page.open_page('https://www.bbc.com/news')

    def test_promo_image(self, driver_chrome, bbs_website):  # 1
        """Checking that elements are clickable"""
        page = BBCNewsPage(driver_chrome)

        promo_image_css = page.wait_for_clicable(
            page.locator_promo_image_css)
        promo_image_xpath = page.wait_for_clicable(
            page.locator_promo_image_xpath)

        assert EC.element_to_be_clickable((promo_image_css, promo_image_xpath))

    def test_homepage_link(self, driver_chrome, bbs_website):  # 2
        """Checking that all elements are displayed on the page"""

        page = BBCNewsPage(driver_chrome)
        homepage_link_css = page.wait_for_clicable(
            page.locator_homepage_link_css)
        homepage_link_xpath = page.wait_for_clicable(
            page.locator_homepage_link_xpath)
        assert EC.visibility_of_all_elements_located((
            homepage_link_css, homepage_link_xpath))

    def test_link_sport(self, driver_chrome, bbs_website):  # 3
        """Checking that this is a link"""

        page = BBCNewsPage(driver_chrome)
        page.assert_value_in_element_attribute(
            page.locator_link_sport_css, 'href', 'https://www.bbc.com/sport')
        page.assert_value_in_element_attribute(
            page.locator_link_sport_xpath, 'href', 'https://www.bbc.com/sport')

    def test_elements_from_site_header(self, driver_chrome, bbs_website):  # 4
        """Checking that all elements from the site header are clickable"""

        page = BBCNewsPage(driver_chrome)
        page.assert_element_from_the_site_header_clickable(
            page.list_css_elements(), page.list_xpath_elements())
