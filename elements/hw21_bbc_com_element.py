from selenium.webdriver.common.by import By

from helpers.base import BasePage


class BBC(BasePage):
    # for task1
    # 1
    locator_promo_image_xpath = By.XPATH, '//*[@id="orb-header"]/div/div[1]'
    locator_promo_image_css = By.CSS_SELECTOR, \
        '[class="orb-nav-section orb-nav-blocks"]'
    # 2
    locator_homepage_link_css = By.CSS_SELECTOR, '[id="homepage-link"]'
    locator_homepage_link_xpath = By.XPATH, '//*[@id="homepage-link"]'
    # 3
    locator_link_sport_css = By.CSS_SELECTOR, \
        'header>div>div>nav>ul>li>[href="https://www.bbc.com/sport"]'
    locator_link_sport_xpath = By.XPATH, \
        '//header//div//div//nav//ul//li//a[@href="https://www.bbc.com/sport"]'
    # 4
    # CSS
    locator_home_css = By.CSS_SELECTOR, \
        'header>div>div>div>nav>ul>li>[href="/news"]'
    locator_climate_css = By.CSS_SELECTOR, \
        'header>div>div>div>nav>ul>li>[href="/news/science_and_environment"]'
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
    # XPATH
    locator_home_xpath = By.XPATH, \
        '//header//div//div//div//nav//ul//li//a[@href="/news"]'
    locator_climate_xpath = By.XPATH, \
        '//*[@id="orb-modules"]/header/div[2]/div/div[1]/nav/ul/li[10]/a'
    locator_world_xpath = By.XPATH, \
        '//header//div//div//div//nav//ul//li//a[@href="/news/world"]'
    locator_business_xpath = By.XPATH, \
        '//header//div//div//div//nav//ul//li//a[@href="/news/business"]'
    locator_science_xpath = By.XPATH, \
        '//header//div//div//div//nav//ul//li//a[@href="/news/science_and_' \
        'environment"]'
    locator_entertainment_xpath = By.XPATH, \
        '//header//div//div//div//nav//ul//li//a[@href="/news/entertainment' \
        '_and_arts"]'
    locator_world_radio_and_tv_xpath = By.XPATH, \
        '//header//div//div//div//nav//ul//li//a[@href="/news/world_radio_a' \
        'nd_tv"]'
