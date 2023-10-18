import pytest
from selenium.webdriver.support import expected_conditions as EC

from base import wait_for_clicable_css, wait_for_clicable_xpath
from conftest import driver_chrome


# создать минимум пять тестов для выбранного вами сайта
# добавить документацию к тестам, чтобы можно было понять о чем тест


# Задание 1:
#
# 1. Открыть сайт http://thedemosite.co.uk/login.php
#
# 2. Ввести имя в поле username
#
# 3. Ввести пароль в поле password
#
# 4. Нажать на кнопку Test Login
#
# 5. Проверить, что Successful Login отображаются
#
# Задание 2
#
# 1. Открыть сайт http://demo.guru99.com/test/newtours/register.php
#
# 2. Заполнить все поля
#
# 3. Нажать кнопку Submit
#
# 4. Проверить, что отображается правильно имя и фамилия
#
# 5. Проверить, что отображается правильно username


locator_the_cross = 'main>div>div>div>[aria-label="Close"]'
locator_profile = 'nav>div>ul>li>[href="#loginModal"]'
locator_profile_authorized_user = '[class="nav-link d-flex align-items' \
                                  '-center"]'
locator_login = '[id="loginEmail"]'
locator_password = '[id="loginPassword"]'
locator_enter = '[class="form-group mt-5"]>[class="loginSubmit submitBtn mai' \
                'nBgColor"]'
locator_basket = '[class="nav-link d-flex align-items-center pl-2 pr-3"]'
locator_favorites = '[class="nav-item d-none d-xl-block"]>[href="/account' \
                    '#favorites"]'
locator_name_authorized_user = '[class="dropdown-menu show"]>[class="user-' \
                               'name"]'
locator_vk_icon = '[class="social-link"]>[src="https://www.kfc.by/admin/' \
                  'files/4475.svg"]'
locator_reject_cookies = '[class="tap decline js-close"]'
locator_orders = '[class="nav-item d-none d-xl-block"]>[href="/tracker"]'
locator_add_to_basket_button = ''
locator = '//*[@id="categories-panels"]/div[1]/div[2]/div[2]/div/div[6]/div' \
          '/div/div/div[3]/div/div[3]'
#############################
text_login = 'vita-sc2@mail.ru'  # test@mail.ru  введите логин
text_password = 'Zpo230742Er'  # 12345678        введите пароль


@pytest.fixture(scope='function')
def authorization_kfc(driver_chrome):
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
    a = driver_chrome.get('https://www.kfc.by')
    the_cross = wait_for_clicable_css(driver_chrome, locator_the_cross)
    the_cross.click()
    profile = wait_for_clicable_css(driver_chrome, locator_profile)
    profile.click()
    login = wait_for_clicable_css(driver_chrome, locator_login)
    login.send_keys(text_login)
    password = wait_for_clicable_css(driver_chrome, locator_password)
    password.send_keys(text_password)
    enter = wait_for_clicable_css(driver_chrome, locator_enter)
    enter.click()
    the_cross = wait_for_clicable_css(driver_chrome, locator_the_cross)
    the_cross.click()
    profile = wait_for_clicable_css(
        driver_chrome, locator_profile_authorized_user)


class TestKFC:

    def test_visibility_and_clickability_of_buttons(self, driver_chrome,
                                                    authorization_kfc):
        """
        Precondition: the user must be logged in to the site
        'https://www.kfc.by' !
        Checking the display and clickability of buttons available on the page
        after user authorization
        """
        basket = wait_for_clicable_css(driver_chrome, locator_basket)
        orders = wait_for_clicable_css(driver_chrome, locator_orders)
        favorites = wait_for_clicable_css(driver_chrome, locator_favorites)

        assert EC.visibility_of(basket and orders and favorites) \
               and EC.element_to_be_clickable(basket and orders and favorites)

    def test_authorized_user(self, driver_chrome, authorization_kfc):
        """
        Precondition: the user must be logged in to the site
        'https://www.kfc.by' !
        Checking that the user is logged in to the site by viewing his
        user-name in the profile section.
        """
        profile = wait_for_clicable_css(
            driver_chrome, locator_profile_authorized_user)
        profile.click()
        name_authorized_user = wait_for_clicable_css(
            driver_chrome, locator_name_authorized_user)

        assert EC.visibility_of_element_located(name_authorized_user)

    def test_vk_icon(self, driver_chrome):
        """
        Checking that after clicking on the "vk" logo button, the desired page
        opened
        """
        driver_chrome.get('https://www.kfc.by')
        the_cross = wait_for_clicable_css(driver_chrome, locator_the_cross)
        the_cross.click()

        reject_cookies = wait_for_clicable_css(
            driver_chrome, locator_reject_cookies)
        reject_cookies.click()
        vk_icon = wait_for_clicable_css(driver_chrome, locator_vk_icon)
        vk_icon.click()
        driver_chrome.switch_to.window(driver_chrome.window_handles[1])
        link_to_click_vk_icon = driver_chrome.current_url
        link_to_vk_expected = 'https://vk.com/kfcbelarusofficial'

        assert link_to_click_vk_icon == link_to_vk_expected



    def test_a(self, driver_chrome, authorization_kfc):
        """
        Сделать заказ
        """
        driver_chrome.get('https://www.kfc.by/menu')
        add_to_basket_button = wait_for_clicable_xpath(driver_chrome,
                                                 locator_add_to_basket_button)

