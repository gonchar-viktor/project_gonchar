import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

logo = 'nav>div>div>a>[class="logo-img"]'
the_cross = 'main>div>div>div>[aria-label="Close"]'


class TestKFC:
    def test_logo_displayed(self, driver_chrome):
        """
        The test opens the main page of the site, closes the pop-up banner
        and checks the visibility of the logo
        Тест открывает главную страницу сайта, закрывает всплывающий баннер
        и проверяет видимость логотипа
        """
        driver_chrome.get('https://www.kfc.by')
        locator_the_cross = driver_chrome.find_element(By.CSS_SELECTOR,
                                                       the_cross)
        locator_the_cross.click()
        time.sleep(1)  # даю время банеру закрыться для скриншота
        locator_logo = driver_chrome.find_element(By.CSS_SELECTOR, logo)
        driver_chrome.save_screenshot('../tests/logo_displayed_hw19.jpg')

        assert EC.visibility_of(locator_logo)
