from selenium.webdriver.common.by import By


class LoginPageLocators(object):#for now it's just facebook
    """this class holds facebook login page locators"""
    LOGIN_BUTTON = (By.NAME, 'login')
    REGISTRATION_BUTTON = (By.ID, 'u_0_2_Vw')
    EMAIL_TEXTFIELD = (By.NAME,'email')
    PASSWORD_TEXTFIELD = (By.NAME,'pass')
    FORGOTPASSWORD_HYPERLINK = (By.CLASS_NAME,'_6ltj')


class RegistrationPageLocators:#for now it's just facebook
    """this class holds facebook Registration page locators"""
    FIRSTNAME_TEXTFIELD = (By.NAME,'firstname')
    LASTNAME_TEXTFIELD = (By.NAME,'lastname')
    MOBILENUMBER_TEXTFIELD = (By.NAME,'reg_email__')
    EMAILADDRESS_TEXTFIELD = (By.NAME,'reg_email__')
    NEWPASSWORD_TEXTFIELD = (By.NAME,'reg_passwd__')
    DATEOFBIRTH_DAY_SELECTOR = (By.NAME,'birthday_day')
    DATEOFBIRTH_MONTH_SELECTOR = (By.NAME,'birthday_month')
    DATEOFBIRTH_YEAR_SELECTOR = (By.NAME,'birthday_year')
    GENDER_MALE_RADIO = (By.ID, 'u_9_5_4b')
    GENDER_FEMALE_RADIO = (By.ID, 'u_9_4_1')
    GENDER_CUSTOM_RADIO = (By.ID, 'u_9_6_fT')
    GENDER_CUSTOM_PRONOUN_RADIO = (By.ID, 'js_1x4')
    GENDER_CUSTOM_OPTINAL_GENDER_TEXTFIELD = (By.NAME,'custom_gender')
    SIGNUP_BUTTON = (By.NAME, 'websubmit')
    SIGNUP_POPUP = (By.CLASS_NAME, '_n3')