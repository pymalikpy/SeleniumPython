import xlrd
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

workbook = xlrd.open_workbook("C:\\Users\\FN-LT\\Desktop\\DataFile.xlsx")
sheet = workbook.sheet_by_name("registration")

rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount)
print(colCount)

driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/?')
url = driver.find_element(By.ID,'Form_submitForm_subdomain')
fullname = driver.find_element(By.ID,'Form_submitForm_Name')
email = driver.find_element(By.ID,'Form_submitForm_Email')
Phonenum = driver.find_element(By.ID,'Form_submitForm_Contact')



for i in range(1,rowCount):
    urlvalue = str(sheet.cell_value(i,0))
    fullnamevalue = str(sheet.cell_value(i,1))
    emailvalue = str(sheet.cell_value(i, 2))
    Phonenumvalue = str(sheet.cell_value(i, 3))
    print(urlvalue + "  " + fullnamevalue)

    url.clear()
    url.send_keys(urlvalue)
    fullname.clear()
    fullname.send_keys(fullnamevalue)
    email.clear()
    email.send_keys(emailvalue)
    Phonenum.clear()
    Phonenum.send_keys(Phonenumvalue)

    time.sleep(4)


