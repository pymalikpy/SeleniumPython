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

driver.get('https://www.globalsqa.com/demo-site/draganddrop')
time.sleep(3)

driver.find_element(By.ID, 'Accepted Elements').click()
driver.implicitly_wait(2)
driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe['demo-frame lazyloaded']"))
source = driver.find_element(By.XPATH, "//div[@id='draggable']")
#WebDriverWait(driver,5).until(EC.presence_of_element_located(driver.find_element(By.ID, 'draggable')))
# try:
#     source_ex = driver.find_element(By.ID, 'draggable')
# except NoSuchElementException:
#     pass
target = driver.find_element(By.XPATH, "//div[@id='droppable']")
#WebDriverWait(driver,5).until(EC.element_to_be_clickable(driver.find_element(By.ID, 'droppable')))
act_chains = ActionChains(driver)
#act_chains.drag_and_drop(source, target).perform()
act_chains.click_and_hold(source).move_to_element(target).release().perform()
driver.switch_to.default_content()
time.sleep(4)
print(driver.title)
driver.close()