from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//*[@class='header-topline__user-link link-dashed']"
    _email_field = "//*[@id='auth_email']"
    _password_field = "//*[@id='auth_pass']"
    _login_button = "//*[@class='button button_color_navy auth-modal__login-button']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="XPATH")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="XPATH")

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[contains(@class,'header-topline__user-link link-dashed')]  [contains(text(),'Roman')]",
                                       locatorType="xpath")
        print("Login Successful")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//p[contains(text(),' Введен неверный пароль! ')]",
                                       locatorType="xpath")
        # print("Login Failed")
        return result