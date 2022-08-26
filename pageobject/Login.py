from selenium.webdriver.common.by import By
from utilities.Useclass import Useclass


class Login(Useclass):

    def __init__(self, driver):
        self.driver = driver

    email = (By.ID, "email")
    password = (By.ID, "pass")
    login = (By.CSS_SELECTOR, 'button[id= "loginbutton"]')

    def get_email(self, params):
        """
            Method used to send user email
        """
        self.wait_test(Login.email)
        return self.driver.find_element(*Login.email).send_keys(params['username'])

    def get_password(self, params):
        """
                   Method used to send user password
        """
        self.wait_test(Login.password)
        return self.driver.find_element(*Login.password).send_keys(params['password'])

    def button_login(self):
        """
                   Method used to click for login user profile
        """
        self.wait_clickable(Login.login)
        return self.driver.find_element(*Login.login).click()
