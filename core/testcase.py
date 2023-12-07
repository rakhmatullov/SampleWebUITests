import unittest
import configparser

from selenium import webdriver
from appium.webdriver.webdriver import WebDriver

configParser = configparser.RawConfigParser()
configFilePath = r'../config.txt'
configParser.read(configFilePath)
app_url = configParser.get('basic', 'url')
login = configParser.get('basic', 'login')
password = configParser.get('basic', 'password')
wrong_login = configParser.get('basic', 'wrong_login')

class TheTestCase(unittest.TestCase):
    __timeout = 120

    @classmethod
    def setUpClass(cls):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--enable-automation")
        chrome_options.add_argument("--service-startup-timeout=200")
        chrome_options.add_argument("--no-sandbox")
        cls.driver: WebDriver = webdriver.Chrome(
                                       options=chrome_options)
        cls.driver.set_page_load_timeout(cls.__timeout)
        cls.driver.set_script_timeout(cls.__timeout)
        cls.driver.implicitly_wait(cls.__timeout)
        cls.driver.get(app_url)
        cls.driver.maximize_window()

    def get_main_page(self):
        self.driver.get(app_url)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()