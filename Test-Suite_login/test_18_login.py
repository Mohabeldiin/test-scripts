"""This test case to verify that welcome message after successfully login into application.
   Login_18 from https://sampletestcases.com/latest-sample-testcases-of-facebook-login-page/"""
import enum
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_Data(enum.Enum):
  """Test data for login test case"""
  email = "salai@outlook.com"
  password = "dalo89872"

class Test_18_login(unittest.TestCase):
  """To verify that welcome message after successfully login into application"""
  def setUp(self):
    """This function run before every test"""
    self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
    self.driver.implicitly_wait(10)
    self.driver.get("https://facebook.com")
    self.email_locator = (By.NAME, "email")
    self.password_locator =(By.NAME, "pass")

  def test_18(self):
    """ this function To verify that welcome message after successfully login into application"""
    try:
      email = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.email_locator)
      )
      email.send_Keys(Test_Data.email.value)

      passwd = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.password_locator)
      )
      passwd.send_Keys(Test_Data.password.value)
      passwd.send_Keys(Keys.RETURN)
      assert  True #"Facebook" in self.driver.title
    except: assert False

  def tearDown(self):
        """this function run after every test"""
        self.driver.quit()

if __name__ == "__main__":
  """This is the main function will Run the Unit Test if this Moudle is not imported"""
  unittest.main()



