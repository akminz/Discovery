from PageObject.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from TestSetup.conftest import *
from ddt import ddt, data, unpack
from utilities.readFileData import getCSVData, getEXLdata

@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    @data(*getCSVData("../test_data/login_data.csv"))
    #@data(("akminz@gmail.com", "987654"), ("akminz@gmail.com", "987654"))
    @unpack
    def test_validLogin(self, email, password):
        self.lp.login(email, password)
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Valid Login Verification")

    @pytest.mark.run(order=1)
    @data(*getEXLdata("../test_data/invalidLogin.xlsx"))
    @unpack
    def test_invalidLogin(self, email, password):
        self.lp.login(email, password)
        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalidLogin", result, "InValid Login Verification")