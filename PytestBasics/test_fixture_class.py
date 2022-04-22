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

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--incognito")
option.headless = False

option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2})

driver = None

@pytest.fixture(scope='class') # defined a fixture  that has a scope in the class
def init_chrome_driver(request):
    print('-----------------setup----------------')
    ch_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
    request.cls.driver = ch_driver
    ch_driver.implicitly_wait(10)
    ch_driver.delete_all_cookies()
    ch_driver.get("https://www.google.com")
    yield
    print("---------tear down-----------")
    ch_driver.quit()

@pytest.fixture(scope='class')
def init_ff_driver(request):
    print('-----------------setup----------------')
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver
    ff_driver.implicitly_wait(10)
    ff_driver.delete_all_cookies()
    ff_driver.get("https://www.google.com")
    yield
    print("---------tear down-----------")
    ff_driver.quit()

@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_Test:
    pass

class Test_Google_Chrome(Base_Chrome_Test):

    def  test_google_title_chrome(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title=='Google'

@pytest.mark.usefixtures("init_ff_driver")
class Base_Firefox_Test:
    pass

class Test_Reddit(Base_Firefox_Test):

    def test_reddit_title(self):
        self.driver.get("https://www.reddit.com")
        assert self.driver.title is not 'Google'


