import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


WAIT_TIME = 10


@pytest.fixture(scope='function', autouse=True)
def driver_chrome():

    print("\n....start chrome browser for test....")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(WAIT_TIME)

    yield driver
    print("\n....quit chrome browser for test....")
    driver.close()
    driver.quit()


@pytest.fixture(scope='function')
def driver_firefox():

    print("\n....start firefox browser for test....")
    driver = webdriver.Firefox()
    # service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(WAIT_TIME)

    yield driver
    print("\n....quit firefox browser for test....")
    driver.close()
    driver.quit()


@pytest.fixture(scope='function')
def driver_safari():

    print("\n....start safari browser for test....")
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.implicitly_wait(WAIT_TIME)

    yield driver
    print("\n....quit safari browser for test....")
    driver.close()
    driver.quit()



