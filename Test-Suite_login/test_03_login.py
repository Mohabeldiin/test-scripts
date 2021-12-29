"""This test case to verify Login functionality with invalid email address and valid password.
   Login_03 from https://sampletestcases.com/latest-sample-testcases-of-facebook-login-page/"""
import enum
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_Data(enum.Enum):
    """Test data for login test case"""
    email = "lol@gmail.com"
    password = "12345678"


class Test_03_login(unittest.TestCase):
    """verify Login functionality with invalid email id and valid password."""
    def setUp(self):
        """this function run before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.get("https://facebook.com")
        self.email_locator = (By.NAME, "email")
        self.password_locator = (By.NAME, "pass")
        #self.email = self.driver.find_element(*self.email_locator)
        #self.passwd = self.driver.find_element(*self.password_locator)
        
    def test_03_login(self):
        """this function Passing invalid email and vaild password"""
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_locator)
            )
            email.send_keys(Test_Data.email.value)

            passwd = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.password_locator)
            )
            passwd.send_keys(Test_Data.password.value)
            passwd.send_keys(Keys.RETURN)
            assert "Facebook" in self.driver.title
        except: assert False

    
    def tearDown(self):
        """this function run after every test"""
        self.driver.quit()

    
if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()