import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Modules.locator import *

class Test_01_User_Interface(unittest.Testcase):
    """this test Checks all the text boxes, radio buttons, buttons, etc"""

    def setUp(self):
        """this method will be called before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.Registratation_button = self.driver.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.fname_textfield = self.driver.find_element(RegistrationPageLocators.FIRSTNAME_TEXTFIELD)
        self.lname_textfield = self.driver.find_element(RegistrationPageLocators.LASTNAME_TEXTFIELD)
        self.email_textfield = self.driver.find_element(RegistrationPageLocators.EMAILADDRESS_TEXTFIELD)
        self.password_textfield = self.driver.find_element(RegistrationPageLocators.NEWPASSWORD_TEXTFIELD)
        self.signup_button = self.driver.find_element(RegistrationPageLocators.SIGNUP_BUTTON)


    def test_01_1_Registration_Page_UI(self):
        """foo"""
        
        try:
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.Registratation_button)
            )
            self.Registratation_button.click()
            if  EC.presence_of_element_located(By.CLASS_NAME, '_n3'): assert True
        except: assert False
        #finally: assert True
        try: 
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.fname_textfield)
            )
            self.fname_textfield.clear()
            self.fname_textfield.send_keys("Test")
            if self.fname_textfield.text == "Test": assert True
        except: assert False


    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()