# what all things we can do from actions class

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time


option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--incognito")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=option)
driver.implicitly_wait(10)

driver.get('https://www.spicejet.com')
time.sleep(3)
'''move to element'''

addons_ele_css = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]')
addons_ele = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]')
WebDriverWait(driver , 5).until(EC.presence_of_element_located(addons_ele_css))
act_chains = ActionChains(driver)
act_chains.move_to_element(addons_ele).perform()
addons_ele_spiceflex_css = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div[9]/div/a[2]/div/div')
addons_ele_spiceflex = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div[9]/div/a[2]/div/div')
WebDriverWait(driver , 5).until(EC.presence_of_element_located(addons_ele_spiceflex_css))
act_chains.move_to_element(addons_ele_spiceflex).perform()
addons_ele_spiceflex.click()
time.sleep(10)
#driver.implicitly_wait(15)

print(driver.title)
driver.close()

# WebDriverWait(driver, 5).until(EC.element_to_be_clickable(login_ele)).click()

