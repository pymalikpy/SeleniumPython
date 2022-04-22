from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager



browsername = "Microsoft Edge"

if browsername == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())

elif browsername == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

elif browsername == 'Microsoft Edge':
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    print('Please pass correct  browser  name' +  browsername)
    raise Exception("driver is not found")


driver.implicitly_wait(5)
driver.get("https://www.automationstepbystep.com")
print(driver.title)

time.sleep(4)
driver.quit()