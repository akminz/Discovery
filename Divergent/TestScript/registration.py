from PageObject.registrationPage import RegisterPage
from utilities.teststatus import TestStatus
import unittest, pytest
from TestSetup.conftest import *

@pytest.mark.usefixtures("oneTimeSetUp")
class RegisterTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.rp = RegisterPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_registerpage(self):
        self.rp.loadingRegester()
        result = self.rp.verifyRegesterLoad()
        self.ts.markFinal("test_registerpage", result, "register page loading Verification")