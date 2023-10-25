# in less

import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestFirst:

    def test_deleviry(self, driver_chrome):
        driver_chrome.get('https://www.21vek.by/')
        driver_chrome.execute_script(
            "document.getElementById('modal-cookie').style.display = 'none'")

        footer_xpath = (
            By.XPATH, '//*[@id="footer-inner"]/div/div/div[1]/div[1]/div[2]/a')
        footer_locator = driver_chrome.find_element(*footer_xpath)
        driver_chrome.execute_script("arguments[0].scrollIntoView();",
                                     footer_locator)
        footer_locator.click()

        current_url = driver_chrome.current_url
        assert current_url == 'https://www.21vek.by/services/delivery.html'

    def test_check_find_elements(self, driver_firefox):
        driver_firefox.get(
            'https://teachmeskills.by/kursy-programmirovaniya/qa-avtomatizirovannoe-testirovanie-na-python-online')

        time.sleep(5)
        selector = driver_firefox.find_element(By.XPATH, '//*[@type="tel"]')
        driver_firefox.execute_script("arguments[0].scrollIntoView();",
                                      selector)
        assert selector.is_enabled()
