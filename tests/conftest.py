import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    # открытие и закрытие хром браузера

    print("\nstart browser for test..")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    print("\nquit browser..")

    driver.close()
    driver.quit()


# доб фикстуры нескольких браузеров, называть можно browser_chrome or browser_firefox
