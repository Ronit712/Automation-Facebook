import time
from selenium.webdriver.support.wait import WebDriverWait
from pageobject.Logout import Logout
from pageobject.Profile import Profile
from utilities.Baseclass import Baseclass
from pageobject.Login import Login


class TestFB(Baseclass):

    def test_first(self, params):
        WebDriverWait(self.driver, 10)
        log = self.get_logger()

        '''initialize Login page object and send user id and password to login'''

        login = Login(self.driver)
        login.get_email(params)
        login.get_password(params)
        login.button_login()
        log.info("Username and Password taken and Login the user profile")

        '''initialize Profile page object'''

        profile = Profile(self.driver)
        profile.click_button_profile()
        profile.click_button_settings_privacy()
        profile.click_button_settings()
        profile.click_button_privacy()
        time.sleep(4)
        profile.click_manage_profile()

        '''verify the given username,mobile number,check the list of blocked user'''

        name = profile.name_verify().text
        log.info(name)
        try:
            assert (params['user'] in name)
        except Exception as e:
            raise e
        number = profile.verify_number()
        log.info(number.text)
        try:
            assert (number.text in params['mobile'])
        except Exception as e:
            raise e
        self.driver.back()
        profile.click_block()
        profile.click_block_edit()
        profile.see_list()
        lists = profile.get_list()
        count = len(lists)
        log.info(f" total number of block user are {count}")
        profile.close_block()

        ''' Initialize the logout pageobject and logout user profile.'''

        logout = Logout(self.driver)
        logout.get_account()
        logout.click_logout()
        log.info("logout successfully")
