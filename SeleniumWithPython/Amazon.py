from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

c = webdriver.ChromeOptions()
# incognito parameter passed
c.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=c)

driver.get("https://www.amazon.in")
driver.implicitly_wait(10)
elelist = driver.find_elements(By.TAG_NAME, "a")
print(len(elelist))

for i in elelist:
    elelist_text = i.text
    print(elelist_text)
    print(i.get_attribute("href"))