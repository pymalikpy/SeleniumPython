# alerts usually come up from java scripts they are not web elements
# we can check same from alert method in console

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

option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
driver.implicitly_wait(10)

driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.find_element(By.NAME,'proceed').click()
time.sleep(3)
alert =  driver.switch_to.alert
print(alert.text)
alert.accept()
#alert.dismiss()
#alert.send_keys('Hello')
driver.switch_to.default_content()
driver.close()