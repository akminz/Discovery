from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TC1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_t_c1(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/insurance/v1/index.php")
        driver.find_element_by_link_text("Register").click()
        driver.find_element_by_id("user_title").click()
        driver.find_element_by_id("user_title").click()
        driver.find_element_by_id("user_firstname").click()
        driver.find_element_by_id("user_firstname").clear()
        driver.find_element_by_id("user_firstname").send_keys("ashish")
        driver.find_element_by_id("user_surname").click()
        driver.find_element_by_id("user_surname").clear()
        driver.find_element_by_id("user_surname").send_keys("minz")
        driver.find_element_by_id("user_phone").click()
        driver.find_element_by_id("user_phone").clear()
        driver.find_element_by_id("user_phone").send_keys("8007485417")
        driver.find_element_by_id("user_dateofbirth_1i").click()
        Select(driver.find_element_by_id("user_dateofbirth_1i")).select_by_visible_text("1980")
        driver.find_element_by_id("user_dateofbirth_1i").click()
        driver.find_element_by_id("user_dateofbirth_2i").click()
        Select(driver.find_element_by_id("user_dateofbirth_2i")).select_by_visible_text("April")
        driver.find_element_by_id("user_dateofbirth_2i").click()
        driver.find_element_by_id("user_dateofbirth_3i").click()
        Select(driver.find_element_by_id("user_dateofbirth_3i")).select_by_visible_text("18")
        driver.find_element_by_id("user_dateofbirth_3i").click()
        driver.find_element_by_id("user_licenceperiod").click()
        Select(driver.find_element_by_id("user_licenceperiod")).select_by_visible_text("5")
        driver.find_element_by_id("user_licenceperiod").click()
        driver.find_element_by_id("user_occupation_id").click()
        Select(driver.find_element_by_id("user_occupation_id")).select_by_visible_text("Engineer")
        driver.find_element_by_id("user_occupation_id").click()
        driver.find_element_by_id("user_address_attributes_street").click()
        driver.find_element_by_id("user_address_attributes_street").clear()
        driver.find_element_by_id("user_address_attributes_street").send_keys("A")
        driver.find_element_by_id("user_address_attributes_city").click()
        driver.find_element_by_id("user_address_attributes_city").clear()
        driver.find_element_by_id("user_address_attributes_city").send_keys("B")
        driver.find_element_by_id("user_address_attributes_county").click()
        driver.find_element_by_id("user_address_attributes_county").clear()
        driver.find_element_by_id("user_address_attributes_county").send_keys("C")
        driver.find_element_by_id("user_address_attributes_postcode").clear()
        driver.find_element_by_id("user_address_attributes_postcode").send_keys("440147")
        driver.find_element_by_id("user_user_detail_attributes_email").click()
        driver.find_element_by_id("user_user_detail_attributes_email").clear()
        driver.find_element_by_id("user_user_detail_attributes_email").send_keys("akminz@gmail.com")
        driver.find_element_by_id("user_user_detail_attributes_password").click()
        driver.find_element_by_id("user_user_detail_attributes_password").clear()
        driver.find_element_by_id("user_user_detail_attributes_password").send_keys("1234567")
        driver.find_element_by_id("user_user_detail_attributes_password_confirmation").click()
        driver.find_element_by_id("user_user_detail_attributes_password_confirmation").clear()
        driver.find_element_by_id("user_user_detail_attributes_password_confirmation").send_keys("1234567")
        driver.find_element_by_id("resetform").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()