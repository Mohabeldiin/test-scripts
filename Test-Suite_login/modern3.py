"""this test case To verify Login functionality with Blank email."""
import unittest
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestData(object):
    """foo"""
    email = ""


class Modern(unittest.TestCase):
    def setUp(self):
        """this method will be called before every test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.modern-academy.edu.eg/')
        self.StudentPortal_locator = "Student Portal"
        self.email_locator = "ctl00_Main_txtEmail"
        self.Login_locator = "ctl00_Main_btnLoginEmail"

    def test_login(self):
        """this method will test the login functionality"""
        try:
            self.student_portal = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, self.StudentPortal_locator))
            )
            self.student_portal.click()
        except exceptions.TimeoutException as ex:
            print("Timed out waiting for page to load")
            print(ex)
            self.assertTrue(False)
        except exceptions.NoSuchElementException as ex:
            print("Page did not load")
            print(ex)
            self.assertTrue(False)
        except exceptions.ElementNotInteractableException as ex:
            print("Element not interactable")
            print(ex)
            self.assertTrue(False)
        except AssertionError as ex:
            print("Assertion error")
            print(ex)
            self.assertTrue(False)

        try:
            self.email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.email_locator))
            )
            self.email.send_keys(TestData.email)
        except exceptions.TimeoutException as ex:
            print("Timed out waiting for page to load")
            print(ex)
            self.assertTrue(False)
        except exceptions.NoSuchElementException as ex:
            print("Page did not load")
            print(ex)
            self.assertTrue(False)

        try:
            self.login = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.Login_locator))
            )
        except exceptions.TimeoutException as ex:
            print("Timed out waiting for page to load")
            print(ex)
            self.assertTrue(False)
        except exceptions.NoSuchElementException as ex:
            print("Page did not load")
            print(ex)
            self.assertTrue(False)


    def tearDown(self):
        """this method will be called after every test"""
        self.driver.quit()







if __name__ == '__main__':
    unittest.main()