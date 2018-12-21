import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import WebDriverException

class EnvironmentSetup(unittest.TestCase):

    def setUp(self):
        path = '../Resources/drivers/chromedriver.exe'
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.accept_untrusted_certs = True
        options.assume_untrusted_cert_issuer = True
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-impl-side-painting")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-seccomp-filter-sandbox")
        options.add_argument("--disable-breakpad")
        options.add_argument("--disable-cast")
        options.add_argument("--disable-cast-streaming-hw-encoding")
        options.add_argument("--disable-cloud-import")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-session-crashed-bubble")
        options.add_argument("--disable-ipv6")
        options.add_argument("--allow-http-screen-capture")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(executable_path=path, chrome_options=options)
        self.driver.implicitly_wait(20)

    def tearDown(self):
        if self.driver != None:
            self.driver.close()
            self.driver.quit()