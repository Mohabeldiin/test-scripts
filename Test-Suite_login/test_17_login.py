"""This test case To verify that entered multiple times incorrect passwords.
   Login_17 from https://sampletestcases.com/latest-sample-testcases-of-facebook-login-page/"""
import enum
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Data(enum.Enum):
    """Test data for login test case"""
    email = "lol@gmail.com"
    password = "12345678"

class Test_17_login(unittest.TestCase):
    """To verify that entered multiple times incorrect passwords."""
    def setUp(self):
        """this function run before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.get("https://facebook.com")
        self.email_locator = (By.NAME, "email")
        self.password_locator = (By.NAME, "pass")

    def test_17(self):
        """To verify that entered multiple times incorrect passwords."""
        
        try:
               
                for i in range(0,3):
                    passwd = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(self.password_locator)
                        )
                    passwd.send_keys(Test_Data.password.value)
                    passwd.send_keys(Keys.RETURN)
                    time.sleep(15)
                    
        except: assert False

    def tearDown(self):
        """this function run after every test"""
        self.driver.quit()
        
if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()        
        


