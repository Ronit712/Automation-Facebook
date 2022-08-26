from selenium.webdriver.common.by import By
from utilities.Useclass import Useclass


class Logout(Useclass):
    click_account = (By.CSS_SELECTOR, 'div[class="om3e55n1 alzwoclg"]')
    button_logout = (By.XPATH, "//span[text()='Log Out']")

    def __init__(self, driver):
        self.driver = driver

    def get_account(self):
        """
            Method used to click on user account
        """
        self.wait_clickable(Logout.click_account)
        return self.driver.find_element(*Logout.click_account).click()

    def click_logout(self):
        """
            Method used to click for logout user profile
        """
        self.wait_clickable(Logout.button_logout)
        return self.driver.find_element(*Logout.button_logout).click()
