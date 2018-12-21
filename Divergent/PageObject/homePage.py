import utilities.custom_logger as cl
import logging
from PageObject.basepage import BasePage

class HomePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Home Page Locators
    register_link = "//*[@class='content']/a[@class='btn btn-default']"
    email = "// form[ @ id = 'login-form'] / div[1] / input[ @ id = 'email']"
    password = "// form[ @ id = 'login-form'] / div[2] / input[ @ id = 'password']"
    Login = "// form[ @ id = 'login-form'] / div[3] / input[ @class ='btn btn-default']"

    def getRegister(self):
        self.isElementPresent(locator=self.register_link, locatorType="xpath")
        self.elementClick(locator=self.register_link, locatorType="xpath")

    def enterEmailId(self,email):
        self.sendKeys(email, locator=self.email, locatorType="xpath")

    def enterPassword(self,pasword):
        self.sendKeys(pasword, locator=self.password, locatorType="xpath")

    def logInbutton(self):
        self.elementClick(locator=self.Login, locatorType="xpath")