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
# driver.get('https://app.hubspot.com/login/')
# print(driver.title)
# wait= WebDriverWait(driver,3)
# email_id = wait.until(EC.presence_of_element_located((By.ID,'username')))
# email_id.send_keys('test@gmail.com')
# driver.find_element(By.ID,'password').send_keys('abc123')
# time.sleep(3)

# driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
# driver.find_element(By.NAME,'proceed').click()
# wait=WebDriverWait(driver,10)
# alert=wait.until(EC.alert_is_present())
# time.sleep(2)
# print(alert.text)
# alert.accept()
# driver.close()

driver.get('https://app.hubspot.com/login/')
wait= WebDriverWait(driver,10)
Signup_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Sign up')))
print(Signup_link.text)
Signup_link.click()
time.sleep(3)
first_name= wait.until(EC.visibility_of_element_located((By.ID,'UIFormControl-2')))
first_name.send_keys('Pinchu dada')
time.sleep(3)