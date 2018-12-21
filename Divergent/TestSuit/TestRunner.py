import unittest
import HtmlTestRunner
from TestScript.login import LoginTests

# get all tests
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTests)

# create a test-suite
test = unittest.TestSuite([login_test])

#open the report file
outfile	= open("./log/SmokeTestReport.html", "w")

#configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(output=outfile, report_title='Test Report', descriptions='test')
#run the suite using HTMLTestRunner
runner.run(test)