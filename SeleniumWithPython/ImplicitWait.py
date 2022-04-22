#Dynamic wait is of two types
# implict and webdriver(explicit) waits


from selenium  import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from  selenium.webdriver.common.by import By
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
    "profile.default_content_setting_values.notifications": 2
})
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
# driver.implicitly_wait(10)

driver.get('https://app.hubspot.com/login/')
time.sleep(2)
driver.find_element(By.ID,'username').send_keys('pinchudada@gmail.com')
time.sleep(2)
