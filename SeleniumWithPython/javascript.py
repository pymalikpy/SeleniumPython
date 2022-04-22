# java scripts is a utility,available in selenium python
# used  for some  tasks that are not done by common methods

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
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=option)

driver.implicitly_wait(10)

driver.get('https://app.hubspot.com/login/')
# best_sellers = driver.find_element(By.LINK_TEXT,'Best Sellers')
# driver.execute_script("arguments[0].click();", best_sellers)
# title = driver.execute_script("return document.title;")
# print(title)
# driver.execute_script("history.go(0);")
# driver.execute_script("alert ('hello selenium');")
# inner_text = driver.execute_script("return document.documentElement.innerText;")
# print(inner_text)
# driver.execute_script("arguments[0].style.border = '3px solid red'",best_sellers)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# books = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[1]/h2')
# driver.execute_script("arguments[0].scrollIntoView(true);",books)
# print(driver("return navigator.useragent;"))
username=driver.find_element(By.ID,'username')

driver.execute_script("arguments[0].value='pinchu dada';",username)
time.sleep(3)
