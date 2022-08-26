import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.usefixtures("setup")
class Useclass:

    def wait_test(self, path):
        """
            This wait is WebDriverWait along with expected condition where
            this wait used to wait for whether element of given locator
            is present or not.If not then raise exception.
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located(path))
        except Exception as e:
            self.log.info(f"{path} is not present to locate")
            raise e

    def wait_clickable(self, path):
        """
            This wait is WebDriverWait along with expected condition where
            this wait used to wait for whether element of given locator
            is clickable or not.If not then raise exception.The locator pass
            through from different page objects
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(path))
        except Exception as e:
            self.log.info(f"{path} is not clickable")
            raise e

    def verify_test(self, path):
        """
            This wait is WebDriverWait along with expected condition where
            this wait used to wait for whether all elements of given locator
            presence or not.If not then raise exception.The locator pass
            through from different page objects
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_all_elements_located(path))
        except Exception as e:
            self.log.info(f"{path} is not present to locate all elements")
            raise e

    def is_present(self, path):
        """
            Method used to return search path enable or not
        """
        search_present = False
        search = bool(path)
        if search:
            search_present = True
        return search_present

    def check_exists_by_xpath(self, path):
        """
            Method used to return element in the path present or not
        """
        try:
            self.driver.find_element(By.XPATH, path)
        except NoSuchElementException:
            return False
        return True
