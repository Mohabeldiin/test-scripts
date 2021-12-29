import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_01_login(unittest.TestCase):
    """foo"""
    def setUp(self):
        """this function run before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.get("https://facebook.com")
        self.email_locator = (By.NAME, "email")
        self.passwd_locator = (By.NAME, "pass")
        
    def test_01(self):
        """this function Passing valid phone and password"""
        try:
            email = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located(self.email_locator)
                )
            email.send_keys("lol67@gmail.com")
            email.send_keys(Keys.TAB)
            assert EC.element_located_to_be_selected(self.passwd_locator)
        except: assert False
    
    
    def tearDown(self):
        """this function run after every test"""
        self.driver.quit()

if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()