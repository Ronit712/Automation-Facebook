from selenium.webdriver.common.by import By
from utilities.Useclass import Useclass


class Profile(Useclass):

    def __init__(self, driver):
        self.driver = driver

    button_profile = (By.CSS_SELECTOR, 'div[class = "om3e55n1 alzwoclg"]')
    button_settings_privacy = (By.XPATH, '//span[normalize-space()="Settings & privacy"]')
    button_settings = (By.XPATH, '//div[@class="jroqu855 nthtkgg5"]/span[text() = "Settings"]')
    button_privacy = (By.XPATH, '//span[text()="Privacy"]')
    manage_profile = (By.XPATH, '//a[@href = "/me/about/"]')
    verify_no = (By.XPATH, '(//div[@class="n3t5jt4f oog5qr5w k1z55t6l pbevjfx6 laatuukc"])[3]')
    verify_name = (By.XPATH, '//div[@class="mfn553m3 th51lws0"]/span/div/h1')
    button_block = (By.XPATH, '//span[text()="Blocking"]')
    button_block_edit = (By.XPATH, '(//div[@aria-label="Edit"])[2]')
    block_list = (By.XPATH, '//span[text()="See your blocked list"]')
    total_list = (By.CSS_SELECTOR, 'div[class="h8391g91 m0cukt09 kpwa50dg ta68dy8c b6ax4al1"]')
    button_close = (By.CSS_SELECTOR, 'div[class="b0ur3jhr facqkgn9 s8sjc6am h28iztb5"]')

    def click_button_profile(self):
        """
            Method used to click user profile account
        """
        self.wait_clickable(Profile.button_profile)
        return self.driver.find_element(*Profile.button_profile).click()

    def click_button_settings_privacy(self):
        """
            Method used to click settings and privacy button in user account
        """
        self.wait_clickable(Profile.button_settings_privacy)
        if self.is_present(Profile.button_profile):
            self.driver.find_element(*Profile.button_settings_privacy).click()

        else:
            self.log.info("check click_button_profile method")

    def click_button_settings(self):
        """
            Method used to click settings button in user account
        """
        self.wait_clickable(Profile.button_settings)
        if self.check_exists_by_xpath(Profile.button_settings_privacy[1]):
            self.driver.find_element(*Profile.button_settings).click()

        else:
            self.log.info("check click_button_settings_privacy method")

    def click_button_privacy(self):
        """
            Method used to click privacy button in user account
        """
        self.wait_clickable(Profile.button_privacy)
        if self.is_present(Profile.button_settings):
            self.driver.find_element(*Profile.button_privacy).click()

        else:
            self.log.info("check click_button_settings method")

    def click_manage_profile(self):
        """
            Method used to click manage profile button in user account
        """
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[0])
        self.wait_test(Profile.manage_profile)
        return self.driver.find_element(*Profile.manage_profile).click()

    def verify_number(self):
        """
            Method used to verify the mobile number of given user
        """
        self.verify_test(Profile.verify_no)

        return self.driver.find_element(*Profile.verify_no)

    def name_verify(self):
        """
            Method used to verify the name of given user
        """
        self.verify_test(Profile.verify_name)
        return self.driver.find_element(*Profile.verify_name)

    def click_block(self):
        """
            Method used to click block button of user profile
        """
        self.wait_clickable(Profile.button_block)
        if self.check_exists_by_xpath(Profile.button_privacy[1]):
            self.driver.find_element(*Profile.button_block).click()

        else:
            self.log.info("check click_button_privacy method")

    def click_block_edit(self):
        """
            Method used to click edit button of user profile
        """
        self.wait_clickable(Profile.button_block_edit)
        if self.check_exists_by_xpath(Profile.button_block[1]):
            self.driver.find_element(*Profile.button_block_edit).click()

        else:
            self.log.info("check click_button_block method")

    def see_list(self):
        """
            Method used to see all blocked person list of user profile
        """
        self.verify_test(Profile.block_list)
        if self.check_exists_by_xpath(Profile.button_block_edit[1]):
            self.driver.find_element(*Profile.block_list).click()

        else:
            self.log.info("check click_button_block_edit method")

    def get_list(self):
        """
            Method used to get all blocked person list of user profile
        """
        self.verify_test(Profile.total_list)
        return self.driver.find_elements(*Profile.total_list)

    def close_block(self):
        """
            Method used to close block section of user profile
        """
        self.wait_clickable(Profile.button_close)
        if self.is_present(Profile.block_list[1]):
            self.driver.find_element(*Profile.button_close).click()

        else:
            self.log.info("check click_button_block_list method")
