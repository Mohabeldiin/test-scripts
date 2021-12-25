import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Test_13_login(unittest.TestCase):
    """foo"""
    def setUp(self):
        """this function run before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get("https://facebook.com")
        self.driver.implicitly_wait(10)
        
    def test_01(self):
        """this function verify of the length email and password"""
        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("lol67237482764781267757c4nfnhunecbyibiasaiortgv@gmail.com")
        passwd = self.driver.find_element(By.NAME, "pass")
        passwd.send_keys("123456789787239774277486896428462bncn849")
        passwd.send_keys(Keys.RETURN)
    
    
    def tearDown(self):
        """this function run after every test"""
        self.driver.quit()