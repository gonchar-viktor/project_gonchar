from pages.hw21_main_page import MainPage21HW
from selenium.webdriver.support import expected_conditions as EC


class BBCNewsPage(MainPage21HW):

    def list_css_elements(self):
        home_css = self.wait_for_clicable(self.locator_home_css)
        climate_css = self.wait_for_clicable(self.locator_climate_css)
        world_css = self.wait_for_clicable(self.locator_world_css)
        business_css = self.wait_for_clicable(self.locator_business_css)
        science_css = self.wait_for_clicable(self.locator_science_css)
        entertainment_css = self.wait_for_clicable(
            self.locator_entertainment_css)
        world_radio_and_tv_css = self.wait_for_clicable(
            self.locator_world_radio_and_tv_css)

        return [home_css, climate_css, world_css, business_css, science_css,
                entertainment_css, world_radio_and_tv_css]

    def list_xpath_elements(self):
        home_xpath = self.wait_for_clicable(self.locator_home_xpath)
        climate_xpath = self.wait_for_clicable(self.locator_climate_xpath)
        world_xpath = self.wait_for_clicable(self.locator_world_xpath)
        business_xpath = self.wait_for_clicable(self.locator_business_xpath)
        science_xpath = self.wait_for_clicable(self.locator_science_xpath)
        entertainment_xpath = self.wait_for_clicable(
            self.locator_entertainment_xpath)
        world_radio_and_tv_xpath = self.wait_for_clicable(
            self.locator_entertainment_xpath)

        return [home_xpath, climate_xpath, world_xpath, business_xpath,
                science_xpath, entertainment_xpath, world_radio_and_tv_xpath]

    @staticmethod
    def assert_element_from_the_site_header_clickable(val1, val2):
        for i in val1:
            assert EC.element_to_be_clickable(i)

        for o in val2:
            assert EC.element_to_be_clickable(o)
