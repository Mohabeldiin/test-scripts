"""This test case To verify that welcome message after successfully login into application.
   Login_19 from https://sampletestcases.com/latest-sample-testcases-of-facebook-login-page/"""
import enum
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

class Test_Data(enum.Enum):
  """Test data for login test case"""
  email = "Salsko989@gmail.com"
  password = ""

class Test_19_login(unittest.TestCase):
  """To verify that welcome message after successfully login into application."""
  def setUp(self):
    """This function run before every test"""
    self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
    self.driver.implicitly_wait(10)
    self.driver.get("https://facebook.com")
    self.email_locator = (By.NAME, "email")
    self.password_locator = (By.NAME, "pass")
    self.Forgottenpassword_locator = (By.CLASS_NAME, "_6ltj")

  def test_19(self):
    """verify that welcome message after successfully login into application."""
    try:
      forogtten = WebDriverWait(self.driver, 10).until(
        Ec.presence_of_element_located(self.Forgottenpassword_locator)
      )
      forogtten.send_Keys(Keys.RETURN)
    except: assert False

  def tearDown(self):
    """This function run after every test"""
    self.driver.quit()

if __name__ == "__main__":
  """This is the main function will Run the Unit Test if this Module is not imported"""
  unittest.main()

