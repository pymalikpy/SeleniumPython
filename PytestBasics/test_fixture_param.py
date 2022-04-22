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

from webdriver_manager.firefox import GeckoDriverManager

# option = Options()
# option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
# option.add_argument("--disable-extensions")
# option.add_argument("--incognito")
# option.headless = False
#
# option.add_experimental_option("prefs", {
#     "profile.default_content_setting_values.notifications": 2})
#
#
#
# @pytest.fixture(params=["chrome","firefox"],scope='class') # defined a fixture  that has a scope in the class and also can define different params  for diff browsers
# def init_driver(request):
#     if  request.param=='chrome':
#         web_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
#     if request.param=='firefox':
#         web_driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
#
#     request.cls.driver = web_driver
#
#     yield
#     web_driver.quit()





@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Google_Chrome(BaseTest):

    def  test_google_title_chrome(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title=='Google'

    def  test_reddit_url(self):
        self.driver.get("https://www.reddit.com")
        assert self.driver.current_url!='Google'




