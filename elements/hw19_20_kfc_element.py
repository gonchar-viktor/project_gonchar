from selenium.webdriver.common.by import By
from helpers.base import BasePage


class KFC(BasePage):
    # links
    link_main_page = 'https://www.kfc.by'
    link_to_vk_expected = 'https://vk.com/kfcbelarusofficial'
    link_account = 'https://www.kfc.by/account#addresses'

    # text
    param_text = 'Минск, Беларусь'

    # hw20
    # fixture
    locator_the_cross = By.CSS_SELECTOR, \
        'main>div>div>div>[aria-label="Close"]'
    locator_profile = By.CSS_SELECTOR, 'nav>div>ul>li>[href="#loginModal"]'
    locator_profile_authorized_user = By.CSS_SELECTOR, \
        '[class="nav-link d-flex align-items-center"]'
    locator_login = By.CSS_SELECTOR, '[id="loginEmail"]'
    locator_password = By.CSS_SELECTOR, '[id="loginPassword"]'
    locator_enter = By.CSS_SELECTOR, \
        '[class="form-group mt-5"]>[class="loginSubmit submitBtn mainBgColor"]'
    locator_basket = By.CSS_SELECTOR, \
        '[class="nav-link d-flex align-items-center pl-2 pr-3"]'
    locator_favorites = By.CSS_SELECTOR, \
        '[class="nav-item d-none d-xl-block"]>[href="/account#favorites"]'
    locator_name_authorized_user = By.CSS_SELECTOR, \
        '[class="dropdown-menu show"]>[class="user-name"]'
    locator_vk_icon = By.CSS_SELECTOR, \
        '[class="social-link"]>[src="https://www.kfc.by/admin/files/4475.svg"]'
    locator_reject_cookies = By.CSS_SELECTOR, '[class="tap decline js-close"]'
    locator_orders = By.CSS_SELECTOR, \
        '[class="nav-item d-none d-xl-block"]>[href="/tracker"]'
    locator_add_to_basket_button = By.XPATH, \
        '//*[@id="categories-panels"]/div[1]/div[2]/div[2]/div/div[6]/div/di' \
        'v/div/div[3]/div/div[3]'
    locator_choosing_a_restaurant = By.CSS_SELECTOR, \
        '[data-content="Выберите ресторан"]'
    locator_restaurant_address = By.CSS_SELECTOR, '[data-store-id="94"]'
    locator_of_the_start_your_order_button = By.CSS_SELECTOR, \
        '[class="startorder-btn mainBgColor mainBorderColor takeAwayModalBtn"]'
    locator_checkout_button = By.CSS_SELECTOR, \
        'div>div>div>[class="checkoutBtn mainBgColor"]'
    locator_checking_the_order_confirmation = By.CSS_SELECTOR, \
        'div>div>div>[class="checkoutBtn mainBgColor"]'
    locator_address_display = By.CSS_SELECTOR, '[id="newAddress_address"]'
    locator_add_address_button = By.CSS_SELECTOR, \
        '[class="addAddressBtn mainBgColor newAddAddress"]'
    # hw19
    locator_logo = By.CSS_SELECTOR, 'nav>div>div>a>[class="logo-img"]'

    text_login = 'введите свой логин'
    text_password = 'введите свой пароль'
