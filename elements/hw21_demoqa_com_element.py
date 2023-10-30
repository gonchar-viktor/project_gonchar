from selenium.webdriver.common.by import By
from helpers.base import BasePage


class DemoqaCom(BasePage):
    # links
    practice_form = 'https://demoqa.com/automation-practice-form'
    text_box = 'https://demoqa.com/text-box'
    elements = "https://demoqa.com/elements"
    radio_button = 'https://demoqa.com/radio-button'
    select_menu = 'https://demoqa.com/select-menu'

    # for task2
    # 1
    locator_checkbox_sports = By.ID, 'hobbies-checkbox-1'
    # 2
    locator_for_message = By.ID, 'permanentAddress'
    locator_element_interactions = By.XPATH, \
        '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[5]'
    # 4
    locator_button_yes = By.ID, 'yesRadio'
    locator_button_impressive = By.ID, 'impressiveRadio'
    locator_button_no = By.ID, 'noRadio'
    # 5
    locator_select_title = By.XPATH, '//div[text()="Select Title"]'
    locator_mr = By.XPATH, '//*[text()="Mr."]'
    # 6
    locator_address = By.CSS_SELECTOR, '[id="currentAddress"]'
    # 7
    locator_present = By.CSS_SELECTOR, '[id="Ad.Plus-300x250"]'
    locator_displayed = By.CSS_SELECTOR, '[id="Ad.Plus-300x250"]'
