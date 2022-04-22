from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--incognito")
option.headless = False

option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2})

def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    driver.quit()

def test_reddit():
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
    driver.implicitly_wait(10)
    driver.get("https://www.reddit.com")
    assert driver.title == "Reddit - Dive into anything"
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com")
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()

def test_instagram():
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com")
    assert driver.title == "Instagram"
    driver.quit()

def test_quora():
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
    driver.implicitly_wait(10)
    driver.get("https://www.quora.com")
    assert driver.title == 'Quora - A place to share knowledge and better understand the world'
    driver.quit()
