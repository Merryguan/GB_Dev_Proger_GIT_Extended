from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open("./Exam/locators.yaml") as f:
        locators = yaml.safe_load(f)
        for locator in locators["xpath"].keys():
            ids[locator] = (By.XPATH, locators["xpath"][locator])
#        for locator in locators["css"].keys():
#            ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None, time=10):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def get_css_property_from_element(self, locator, property, description=None, time=10):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time)
        if not field:
            return None
        try:
            text = field.value_of_css_property(property)
        except:
            logging.exception(f"Exception while get css property from {element_name}")
            return None
        logging.debug(f"We find property {text} in field {element_name}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word,
                                   description="Login field")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word,
                                   description="Password field")

    # CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="Login")

    def click_about_link_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_ABOUT_LINK_BTN"], description="About")

    # GET TEXT
    def get_user_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_HELLO"],
                                          description="user", time=8)

    #CSS Property
    def get_about_title_css(self):
        return self.get_css_property_from_element(TestSearchLocators.ids["LOCATOR_ABOUT_TITLE"],
                                                  "font-size", description="About title")