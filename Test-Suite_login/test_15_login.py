import unittest
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Test_01_login(unittest.TestCase):
    """foo"""
    def setUp(self):
        """this function run before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get("https://facebook.com")
        self.driver.implicitly_wait(10)
        
    def test_01(self):
        """this function Passing valid phone and password"""
        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("lol67@gmail.com")
       """ try:
            
            main = WebDriverWait(self.driver,10).until(
            EC.presence_of_all_elements_located(self.Error_message) 
            )
            if EC.presence_of_all_elements_located(self.Error_message):assert True
        except: assert False"""
            
        tab_key= ActionChains() # was try to know if tab button works
        tab_key.send_keys(keys.TAB)
        tab_key.perform() 
        
        passwd = self.driver.find_element(By.NAME, "pass")
        passwd.send_keys("123456789")
        passwd.send_keys(Keys.RETURN)
    
    
    def tearDown(self):
        """this function run after every test"""
        self.driver.quit()
