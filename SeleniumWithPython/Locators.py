from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

c = webdriver.ChromeOptions()
#incognito parameter passed
c.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=c)
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/")
driver.maximize_window()
print(driver.title)