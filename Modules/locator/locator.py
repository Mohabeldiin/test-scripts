"""this module contains all pages locators 
    NOW: now it contains facebook pages locators
    LATER: it will contain the AI module to auto-detect page elements"""
from selenium.webdriver.common.by import By


class LoginPageLocators(object):  # for now, it's just facebook
    """this class holds facebook login page locators"""
    LOGIN_BUTTON = (By.NAME, "login")
    REGISTRATION_BUTTON = (By.CLASS_NAME, "_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy")
    EMAIL_TEXTFIELD = (By.NAME, "email")
    PASSWORD_TEXTFIELD = (By.NAME, "pass")
    FORGOT_PASSWORD_HYPERLINK = (By.CLASS_NAME, "_6ltj")


class RegistrationPageLocators(object):  # for now, it's just facebook
    """this class holds facebook Registration page locators"""
    FIRSTNAME_TEXTFIELD = (By.NAME, "firstname")
    LASTNAME_TEXTFIELD = (By.NAME, "lastname")
    MOBILE_NUMBER_TEXTFIELD = (By.NAME, "reg_email__")
    EMAIL_ADDRESS_TEXTFIELD = (By.NAME, "reg_email__")
    CONFIRMATION_EMAIL_ADDRESS_TEXTFIELD = (By.NAME, "reg_email_confirmation__")
    NEW_PASSWORD_TEXTFIELD = (By.NAME, "reg_passwd__")
    DATE_OF_BIRTH_DAY_SELECTOR = (By.NAME, "birthday_day")
    DATE_OF_BIRTH_MONTH_SELECTOR = (By.NAME, "birthday_month")
    DATE_OF_BIRTH_YEAR_SELECTOR = (By.NAME, "birthday_year")
    GENDER_MALE_RADIO = (By.ID, "u_9_5_4b")
    GENDER_FEMALE_RADIO = (By.ID, "u_9_4_1")
    GENDER_CUSTOM_RADIO = (By.ID, "u_9_6_fT")
    GENDER_CUSTOM_PRONOUN_RADIO = (By.ID, "js_1x4")
    GENDER_CUSTOM_OPTIONAL_GENDER_TEXTFIELD = (By.NAME, "custom_gender")
    SIGNUP_BUTTON = (By.NAME, "websubmit")
    SIGNUP_POPUP = (By.CLASS_NAME, "_n3")
