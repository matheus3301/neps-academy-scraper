from selenium import webdriver
import src.constants as constants
from time import sleep


class Neps:
    is_logged = False

    def __init__(self, browser: webdriver.Chrome):
        self.__browser = browser
        self.__browser.get(constants.NEPS_URL)
        self.use_english()

    def use_english(self):
        try:
            self.__browser.find_element_by_xpath(
                constants.ENGLISH_BUTTON).click()
        except:
            pass

    def login(self, email, password) -> bool:
        if(self.is_logged):
            return True

        self.__browser.find_element_by_xpath(
            constants.LOGIN_PAGE_BUTTON).click()

        email_input = self.__browser.find_element_by_xpath(
            constants.EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.__browser.find_element_by_xpath(
            constants.PASSWORD_INPUT)
        password_input.send_keys(password)

        self.__browser.find_element_by_xpath(
            constants.LOGIN_MODAL_BUTTON).click()

        sleep(5)
        if(self.__browser.current_url == constants.NEPS_URL+"/dashboard"):
            return True

        return False

    def page_exercises(self):
        pass
