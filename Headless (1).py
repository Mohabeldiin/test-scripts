import enum
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Test_Data(enum.Enum):
    """Test data for login test case"""
    email = "lsssol@gmail.com"
    password = "12345678"


class Test_01_login(unittest.TestCase):
    """verify Login functionality with valid email id and valid password."""
    def setUp(self):
        """this function run before every test"""
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver.exe", options=options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://facebook.com")

    def tearDown(self):
        """this function run after every test"""
        self.driver.quit()

    def test_01_login(self):
        assert "Facebook" in self.driver.title

if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()