from selenium.webdriver.support import expected_conditions as EC

from pages.hw19_20_kfc_page import AuthorizationPage
from conftest import driver_chrome


class TestKFC:
    def test_logo_displayed(self, driver_chrome):
        """
        The test opens the main page of the site, closes the pop-up banner
        and checks the visibility of the logo
        """
        page = AuthorizationPage(driver_chrome)
        page.open_page(page.link_main_page)
        page.driver.implicitly_wait(page.wait_until)
        driver_chrome.save_screenshot('../tests/logo_displayed_hw19.jpg')
        assert EC.visibility_of(page.find_element_func(page.locator_logo))
