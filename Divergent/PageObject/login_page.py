import utilities.custom_logger as cl
import logging
from PageObject.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Home Page Locators
    register_link = "Register"
    email_field = "email"
    password_field = "password"
    Login_button = "//form[@id='login-form']/div[3]/input[@class='btn btn-default']"


    def enterEmail(self, email):
        self.sendKeys(email, self.email_field, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, self.password_field, locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self.Login_button, locatorType="xpath")

    def clickLogOut(self):
        self.elementClick("//form[@class='button_to']/input[@class='btn btn-danger']", locatorType="xpath")


    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@class='content']/h4", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//form[@id='login-form']/div[2]/span/b", locatorType="xpath")
        return result