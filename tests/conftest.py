import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver_chrome():
    # открытие и закрытие chrome browser

    print("\n....start chrome browser for test....")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    print("\n....quit chrome browser for test....")
    driver.close()
    driver.quit()


@pytest.fixture(scope='function')
def driver_firefox():
    # открытие и закрытие firefox browser

    print("\n....start firefox browser for test....")
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    print("\n....quit firefox browser for test....")
    driver.close()
    driver.quit()


@pytest.fixture(scope='function')
def driver_safari():
    # открытие и закрытие safari browser

    print("\n....start safari browser for test....")
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    print("\n....quit safari browser for test....")
    driver.close()
    driver.quit()
