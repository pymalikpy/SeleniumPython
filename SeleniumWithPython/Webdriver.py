from selenium import webdriver
from selenium.webdriver.common.by import By
import time

c = webdriver.ChromeOptions()
#incognito parameter passed
c.add_argument("--incognito")

driver = webdriver.Chrome(executable_path="C:\\Users\\FN-LT\\Desktop\\Personal\\Selenium\\chromedriver_win32 (2)\\chromedriver.exe", options=c)
driver.implicitly_wait(5)


driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.NAME,'q').send_keys('Naveen Automation')
optionsList= driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span ')

print(len(optionsList))

for i in  optionsList:
    print(i.text)
    if i.text =='naveen automationlabs youtube':
        i.click()
        break

print(driver.title)
time.sleep(5)
driver.close()

