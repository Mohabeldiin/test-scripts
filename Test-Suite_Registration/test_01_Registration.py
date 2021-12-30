"""this test Checks all the text boxes, radio buttons, buttons, etc
    TC_01_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ..Modules.locator.locator import LoginPageLocators
from ..Modules.locator.locator import RegistrationPageLocators

class Test_01_User_Interface(unittest.TestCase):
    """this test Checks all the text boxes, radio buttons, buttons, etc"""

    def setUp(self):
        """this method will be called before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.Registratation_button = self.driver.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        self.fname_textfield = self.driver.find_element(*RegistrationPageLocators.FIRSTNAME_TEXTFIELD)
        self.lname_textfield = self.driver.find_element(*RegistrationPageLocators.LASTNAME_TEXTFIELD)
        self.email_textfield = self.driver.find_element(*RegistrationPageLocators.EMAILADDRESS_TEXTFIELD)
        self.password_textfield = self.driver.find_element(*RegistrationPageLocators.NEWPASSWORD_TEXTFIELD)
        self.signup_button = self.driver.find_element(*RegistrationPageLocators.SIGNUP_BUTTON)
        self.sinup_popup = self.driver.find_element(*RegistrationPageLocators.SIGNUP_POPUP)
        self.day_selector = self.driver.find_element(*RegistrationPageLocators.DATEOFBIRTH_DAY_SELECTOR)
        self.month_selector = self.driver.find_element(*RegistrationPageLocators.DATEOFBIRTH_MONTH_SELECTOR)
        self.year_selector = self.driver.find_element(*RegistrationPageLocators.DATEOFBIRTH_YEAR_SELECTOR)
        self.female_radio = self.driver.find_element(*RegistrationPageLocators.GENDER_FEMALE_RADIO)
        self.male_radio = self.driver.find_element(*RegistrationPageLocators.GENDER_MALE_RADIO)
        self.custom_radio = self.driver.find_element(*RegistrationPageLocators.GENDER_CUSTOM_RADIO)
        self.custom_optinal_gender_textfield = self.driver.find_element(*RegistrationPageLocators.GENDER_CUSTOM_OPTINAL_GENDER_TEXTFIELD)


    def test_01_1_Registration_Page_UI(self):
        """this test Checks the presence of all UI elements"""

        try:
            main = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located(self.sinup_popup)
            )
            if EC.presence_of_element_located(self.sinup_popup) : assert True
        except: assert False

        try:
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.Registratation_button)
            )
            self.Registratation_button.click()
            if  EC.presence_of_element_located(self.Registratation_button): assert True
        except: assert False

        try: 
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.fname_textfield)
            )
            self.fname_textfield.clear()
            self.fname_textfield.send_keys("Test")
            if self.fname_textfield.text == "Test": assert True
        except: assert False

        try:
            main = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located(self.lname_textfield)
            )
            self.lname_textfield.clear()
            self.lname_textfield.send_keys("Test")
            if self.lname_textfield.text == "Test": assert True
        except: assert False

        try:
            main = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located(self.email_textfield)
            )
            self.email_textfield.clear()
            self.email_textfield.send_keys("Test@test.com")
            if self.email_textfield.text == "Test@test.com": assert True
        except: assert False
        
        try:
            main = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located(self.password_textfield)
            )
            self.password_textfield.cler()
            self.password_textfield.send_keys("Password!test123&")
            #if self.password_textfi
            if EC.presence_of_element_located(self.password_textfield): assert True
        except: assert False

        try:
            main = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located(self.day_selector)
            )
            self.day_selector.click()
            self.driver.find_element(By.XPATH,'//*[@id="day"]/option[6]').click()
            if EC.presence_of_element_located(self.day_selector): assert True
        except: assert False

        try:
            main = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located(self.month_selector)
            )
            self.day_selector.click()
            self.driver.find_element(By.XPATH,'//*[@id="month"]/option[4]').click()
            if EC.presence_of_element_located(self.month_selector): assert True
        except: assert False

        try:
            main = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located(self.year_selector)
            )
            self.day_selector.click()
            self.driver.find_element(By.XPATH,'//*[@id="year"]/option[25]').click()
            if EC.presence_of_element_located(self.year_selector): assert True
        except: assert False

        try:
            main = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located(self.female_radio)
            )
            self.female_radio.click()
            if EC.presence_of_element_located(self.female_radio): assert True
        except: assert False
        
        try:
            main = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located(self.signup_button)
            )
            self.email_textfield.clear()
            self.signup_button.click()
            if EC.presence_of_element_located(By.ID,'js_545'): assert True
        except: assert False


    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()


if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()

