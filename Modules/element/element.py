from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """ths is a setter method
        
        Args:
            obj: object
            value: value of the attribute
            """
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME,self.locator))
        driver.find_element(By.NAME,self.locator).clear()
        driver.find_element(By.NAME,self.locator).send_keys(value)

    
    def __get__(self, obj, owner):
        """this is a getter method
        
        Args:
            obj: object
            owner: owner of the attribute
        Returns:
            attribute: value of the attribute
            """ 
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME,self.locator))
        element = driver.find_element(By.NAME,self.locator)
        return element.get_attribute("value")