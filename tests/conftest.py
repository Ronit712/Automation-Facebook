from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

from Testdata.tetsdata_fb import Testdata


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption("--username", action="store", help="input useranme")
    parser.addoption("--password", action="store", help="input password")
    parser.addoption("--user", action="store", help="input user")
    parser.addoption("--mobile", action="store", help="input mobile")


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    """
        Set the driver path with base url and return the driver
    """
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service(Testdata.executable_path)
        driver = webdriver.Chrome(service=service_obj)

        driver.get(Testdata.base_url)
        driver.maximize_window()

        request.cls.driver = driver
        yield
        driver.close()


@pytest.fixture
def params(request):
    """
        Set the username,password,user(exactly which is given in
        facebook profile name),mobile for pass the argument.

    """
    params = {'username': request.config.getoption('--username'), 'password': request.config.getoption('--password'),
              'user': request.config.getoption('--user'), 'mobile': request.config.getoption('--mobile')}
    if params['username'] is None and params['password'] is None:
        pytest.skip()
    return params
