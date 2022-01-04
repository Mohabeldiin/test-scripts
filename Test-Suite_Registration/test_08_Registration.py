"""this test case Check the phone number when passing alphanumeric data
    TC_08_Registration from https://www.loginradius.com/blog/async/test-cases-for-registration-and-login-page/"""


import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Test_Data(object):
    """this class holds the test data that is used in this test case"""
    PHONE_NUMBER = "dada5$7567#7"


class Test_08_Registration(unittest.TestCase):
    """Check the phone number when passing alphanumeric data.\n
    1- Enter alphanumeric data in phone field.\n
    2- Click on Register button"""

    def setUp(self):
        """this method will be called before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()
        self.login_form_locator = (By.CLASS_NAME,"_9vtf")
        self.creat_new_account_locator = (By.LINK_TEXT, "Create New Account")

        try:
            if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.login_form_locator)
            ).is_displayed():
                self.creat_new_acount = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.creat_new_account_locator)
                )
                self.creat_new_acount.click()
        except TimeoutException:
            print("\n###############\n",TimeoutException.__doc__ , "\n###############\n")
            assert False

        self.phone_textfiled_locator = (By.NAME,'reg_email__')
        self.sinUp_button_locator = (By.NAME, "websubmit")
        self.textfiled_mandatory_symbol = (By.CLASS_NAME, "_5dbc img sp_98fCI7IVTTz_1_5x sx_e1ddd6")
        self.error_message_locator = (By.ID, "reg_error_inner")

    def test_01_Phone_Number_validation(self):
        """Check the phone number when passing alphanumeric data.\n
        EC: It should not show any validation message."""
        
        try:
            try:
                phone = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.phone_textfiled_locator)
                )
                phone.send_keys(Test_Data.PHONE_NUMBER)
            except AssertionError:
                print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
                assert False
            try:
                sinup = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.sinUp_button_locator)
                )
                sinup.click()
            except AssertionError:
                print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
                assert False
            try:
                if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.error_message_locator)
                ):
                    assert True
                else:
                    print("EC != AC")
                    assert False
            except AssertionError:
                print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
                assert False
        except AssertionError:
            print("\n###############\n",AssertionError.__doc__ , "\n###############\n")
            assert False
        

    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()


if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()