"""this test case Check the required fields by not filling any data"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Modules.locator.locator import *


class Test_02_Registration(unittest.TestCase):
    """1-Do not enter any value in the field.
        2-Click on the Register button."""

    def setUp(self):
        """this method will be called before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def test_01_Required_Fields(self):
        """Check the required fields by not filling any data"""
        pass


    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()