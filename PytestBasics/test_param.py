import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


@pytest.mark.usefixtures("init_driver")
class BaseTest():
    pass


class TestHubSpot(BaseTest):
    @pytest.mark.parametrize("username, password",
                             [('admin123@email.com', 'pass123'),
                              ('prince123@gmail.com', 'prince123'),
                              ('alka124@yahoo.in', 'alka124')
                              ]
                             )
    def test_login(self, username, password):
        """
        This method is used for login to hub spot
        :param username:
        :param password:
        :return:
        """
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID, 'username').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        time.sleep(3)
