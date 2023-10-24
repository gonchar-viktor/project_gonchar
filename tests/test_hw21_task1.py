import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base import wait_for_clicable
from conftest import driver_chrome


# for 1
locator_promo_image_xpath = By.XPATH,\
    '//*[@id="u7191700206677951"]/div/div[1]/div/div/div[1]/div[1]'
locator_promo_image_css = By.CSS_SELECTOR,\
    '[class="gs-c-promo-image gel-1/1 gel-3/4@l gel-3/5@xxl gs-u-float-rig' \
    'ht@l"]'
# for 2
locator_homepage_link_css = By.CSS_SELECTOR, '[id="homepage-link"]'
locator_homepage_link_xpath = By.XPATH, '//*[@id="homepage-link"]'
# for 3
locator_link_sport_css = By.CSS_SELECTOR,\
    'header>div>div>nav>ul>li>[href="https://www.bbc.com/sport"]'
locator_link_sport_xpath = By.XPATH,\
    '//header//div//div//nav//ul//li//a[@href="https://www.bbc.com/sport"]'
# for 4
locator_home_css = By.CSS_SELECTOR, \
    'header>div>div>div>nav>ul>li>[href="/news"]'
locator_climate_css = By.CSS_SELECTOR, \
    'header>div>div>div>nav>ul>li>[href="/news/science-environment-56837908"]'
locator_world_css = By.CSS_SELECTOR, \
    'header>div>div>div>nav>ul>li>[href="/news/world"]'
locator_business_css = By.CSS_SELECTOR, \
    'header>div>div>div>nav>ul>li>[href="/news/business"]'
locator_science_css = By.CSS_SELECTOR, \
    'header>div>div>div>nav>ul>li>[href="/news/science_and_environment"]'
locator_entertainment_css = By.CSS_SELECTOR, \
    'header>div>div>div>nav>ul>li>[href="/news/entertainment_and_arts"]'
locator_world_radio_and_tv_css = By.CSS_SELECTOR, \
    'header>div>div>div>nav>ul>li>[href="/news/world_radio_and_tv"]'

locator_home_xpath = By.XPATH, \
    '//header//div//div//div//nav//ul//li//a[@href="/news"]'
locator_climate_xpath = By.XPATH, \
    '//header//div//div//div//nav//ul//li//a[@href="/news/science-environmen' \
    't-56837908"]'
locator_world_xpath = By.XPATH, \
    '//header//div//div//div//nav//ul//li//a[@href="/news/world"]'
locator_business_xpath = By.XPATH, \
    '//header//div//div//div//nav//ul//li//a[@href="/news/business"]'
locator_science_xpath = By.XPATH, \
    '//header//div//div//div//nav//ul//li//a[@href="/news/science_and_enviro' \
    'nment"]'
locator_entertainment_xpath = By.XPATH, \
    '//header//div//div//div//nav//ul//li//a[@href="/news/entertainment_an' \
    'd_arts"]'
locator_world_radio_and_tv_xpath = By.XPATH,\
    '//header//div//div//div//nav//ul//li//a[@href="/news/world_radio_and_tv"]'


@pytest.fixture(scope='function')
def bbs_website(driver_chrome):
    driver_chrome.get('https://www.bbc.com/news')


class TestBBC:
    def test_promo_image(self, driver_chrome, bbs_website):  # 1
        """Checking that elements are clickable"""

        promo_image_css = wait_for_clicable(
            driver_chrome, locator_promo_image_css)
        promo_image_xpath = wait_for_clicable(
            driver_chrome, locator_promo_image_xpath)
        assert EC.element_to_be_clickable(
            promo_image_css) and EC.element_to_be_clickable(promo_image_xpath)

    def test_homepage_link(self, driver_chrome, bbs_website):  # 2
        """Checking that all elements are displayed on the page"""

        homepage_link_css = wait_for_clicable(
            driver_chrome, locator_homepage_link_css)
        homepage_link_xpath = wait_for_clicable(
            driver_chrome, locator_homepage_link_xpath)

        assert EC.visibility_of_all_elements_located((
            homepage_link_css, homepage_link_xpath))

    def test_link_sport(self, driver_chrome, bbs_website):  # 3
        """Checking that this is a link"""

        link_sport_css = wait_for_clicable(
            driver_chrome, locator_link_sport_css)
        link_sport_xpath = wait_for_clicable(
            driver_chrome, locator_link_sport_xpath)
        a = link_sport_css.get_attribute('href')
        b = link_sport_xpath.get_attribute('href')
        assert (a and b) == 'https://www.bbc.com/sport'

    def test_a(self, driver_chrome, bbs_website):  # 4
        """Checking that all elements from the site header are clickable"""

        home_css = wait_for_clicable(driver_chrome, locator_home_css)
        climate_css = wait_for_clicable(driver_chrome, locator_climate_css)
        world_css = wait_for_clicable(driver_chrome, locator_world_css)
        business_css = wait_for_clicable(driver_chrome,
                                         locator_business_css)
        science_css = wait_for_clicable(driver_chrome, locator_science_css)
        entertainment_css = wait_for_clicable(driver_chrome,
                                              locator_entertainment_css)
        world_radio_and_tv_css = wait_for_clicable(
            driver_chrome, locator_world_radio_and_tv_css)
        #
        home_xpath = wait_for_clicable(driver_chrome, locator_home_xpath)
        climate_xpath = wait_for_clicable(driver_chrome,
                                          locator_climate_xpath)
        world_xpath = wait_for_clicable(driver_chrome,
                                        locator_world_xpath)
        business_xpath = wait_for_clicable(driver_chrome,
                                           locator_business_xpath)
        science_xpath = wait_for_clicable(driver_chrome,
                                          locator_science_xpath)
        entertainment_xpath = wait_for_clicable(
            driver_chrome, locator_entertainment_xpath)
        world_radio_and_tv_xpath = wait_for_clicable(
            driver_chrome, locator_entertainment_xpath)
        tupl = (home_css, climate_css, world_css, business_css, science_css,
                entertainment_css, world_radio_and_tv_css, home_xpath,
                climate_xpath, world_xpath, business_xpath, science_xpath,
                entertainment_xpath, world_radio_and_tv_xpath)
        for i in tupl:
            assert EC.element_to_be_clickable(i)
