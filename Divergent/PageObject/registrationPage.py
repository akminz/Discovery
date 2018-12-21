import utilities.custom_logger as cl
import logging
from PageObject.basepage import BasePage

class RegisterPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Registration Page
    register_link = "Register"
    user_title = "user_title"
    user_firstname = "user_firstname"
    user_surname = "user_surname"
    user_phone = "user_phone"
    birth_year = "user_dateofbirth_1i"
    birth_month = "user_dateofbirth_2i"
    birth_date = "user_dateofbirth_3i"
    licence_period = "user_licenceperiod"
    occupation = "user_occupation_id"
    full = "//form[@id='new_user']/div[2]/div[4]/input[@id='licencetype_t']"
    provisonal = "/form[@id='new_user']/div[2]/div[4]/input[@id='licencetype_f']"
    street = "user_address_attributes_street"
    city ="user_address_attributes_city"
    county = "user_address_attributes_county"
    postcode = "user_address_attributes_postcode"
    email = "user_user_detail_attributes_email"
    password = "user_user_detail_attributes_password"
    password_confirmation = "user_user_detail_attributes_password_confirmation"

    def verifyRegesterLoad(self):
        result = self.isElementPresent("//*[@class='content']/h1", locatorType="xpath")
        return result

    def clickRegisterLink(self):
        self.elementClick(self.register_link, locatorType="id")

    def Reset(self):
        self.elementClick(self.register_link, locatorType="id")
        self.elementClick(self.user_title, locatorType="id")






    # def Registerpage(self):
    #     self.isElementPresent(locator=self.title, locatorType="xpath")
    #
    # def enterCourseName(self, name):
    # self.sendKeys(name, locator=self._search_box)
    # self.elementClick(locator=self._search_course_icon)
    #
    # def selectCourseToEnroll(self, fullCourseName):
    #     self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")
    #
    # def clickOnEnrollButton(self):
    #     self.elementClick(locator=self._enroll_button)
    #
    # def enterCardNum(self, num):
    #     self.switchToFrame(name="__privateStripeFrame4")
    #     self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
    #     self.switchToDefaultContent()
    #
    # def enterCardExp(self, exp):
    #     self.switchToFrame(name="__privateStripeFrame5")
    #     self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
    #     self.switchToDefaultContent()
    #
    # def enterCardCVV(self, cvv):
    #     self.switchToFrame(name="__privateStripeFrame6")
    #     self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
    #     self.switchToDefaultContent()
    #
    # def enterZip(self, zip):
    #     self.switchToFrame(name="__privateStripeFrame7")
    #     self.sendKeys(zip, locator=self._zip, locatorType="name")
    #     self.switchToDefaultContent()
    #
    # def clickAgreeToTermsCheckbox(self):
    #     self.elementClick(locator=self._agree_to_terms_checkbox)
    #
    # def clickEnrollSubmitButton(self):
    #     self.elementClick(locator=self._submit_enroll, locatorType="xpath")
    #
    # def enterCreditCardInformation(self, num, exp, cvv, zip):
    #     self.enterCardNum(num)
    #     self.enterCardExp(exp)
    #     self.enterCardCVV(cvv)
    #     self.enterZip(zip)
    #
    # def enrollCourse(self, num="", exp="", cvv="", zip=""):
    #     self.clickOnEnrollButton()
    #     self.webScroll(direction="down")
    #     self.enterCreditCardInformation(num, exp, cvv, zip)
    #     self.clickAgreeToTermsCheckbox()
    #
    # def verifyEnrollFailed(self):
    #     result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath",
    #                             info="Enroll Button")
    #     return not result