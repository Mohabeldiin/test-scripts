import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Test_10_login(unittest.TestCase):
    """foo"""
    def setUp(self):
        """this function run before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get("https://facebook.com")
        self.driver.implicitly_wait(10)
        
    def test_01(self):
        """this function Passing invalid phone and vaild password"""
        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("76763678888888888")
        passwd = self.driver.find_element(By.NAME, "pass")
        passwd.send_keys("123456789")
        passwd.send_keys(Keys.RETURN)
    
    
    def tearDown(self):
        """this function run after every test"""
        self.driver.quit()
            
if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()