from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """this class holds facebook main page locators"""
    LOGIN_BUTTON = (By.NAME, 'login')
    REGISTRATION_BUTTON = (By.ID, 'u_0_2_Vw')
    EMAIL_TEXTFIELD = (By.NAME,'email')
    PASSWORD_TEXTFIELD = (By.NAME,'pass')
    FORGOTPASSWORD_HYPERLINK = (By.CLASS_NAME,'_6ltj')


class RegistrationPageLocators:
    """foo"""
    FIRSTNAME_TEXTFIELD = (By.NAME,'firstname')
    