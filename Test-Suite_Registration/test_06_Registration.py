"""this test case Check the Email text field that has Email validation
    TC_06_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Test_06_Registration(unittest.TestCase):
    """1- Enter Invalid Emails.
       2- Click on the Register Button.
       Description:
                Check the Email text field that has an Email address without @ symbol.
                Check the Email text field that has a random string instead of a real email.
                Check the Email text field that has @ symbol written in words.
                Check the Email text field that has a missing dot in the email address.
        Test Data:
                1.testgmail.com
                2.test@gmail.com
                3.testAtgmail.com
                4.test@gmailcom"""
    
    def setUp(self):
        """this method will be called before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()


    def test_01_Email_validation(self):
        """Check the Email text field that has an Email address without @ symbol."""
        pass


    def test_02_Email_validation(self):
        """Check the Email text field that has a random string instead of a real email."""
        pass


    def test_03_Email_validation(self):
        """Check the Email text field that has @ symbol written in words."""
        pass


    def test_04_Email_validation(self):
        """Check the Email text field that has a missing dot in the email address."""
        pass


    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()


if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()