from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select


c = webdriver.ChromeOptions()
# incognito parameter passed
c.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=c)

driver.get("https://www.amazon.in")
driver.implicitly_wait(10)

def select_values(element,value):
    select = Select(element)
    select.select_by_visible_text(value)

def select_dropdow_values(dropdownoptionslist,value):
    print(len(dropdownoptionslist))
    for i in dropdownoptionslist:
        print(i.text)
        if i.text=='Baby':
            i.click()
            break

dropdownbox_xpath=driver.find_elements(By.XPATH,'//select[@id="searchDropdownBox"]/option')
select_dropdow_values(dropdownbox_xpath,'Appliances')
time.sleep(2)
select_dropdow_values(dropdownbox_xpath,'Baby')

# dropdownbox = driver.find_element(By.ID, 'searchDropdownBox')
# select_values(dropdownbox,'Books')
#select = Select(dropdownbox)
#select.select_by_visible_text('Books')
#select.select_by_index(9)
#select.select_by_value()
# driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Wings of Fire')
# select=Select(dropdownbox)
# dropdownbox_list = select.options
# print(len(dropdownbox_list))
# for i in dropdownbox_list:
#     print(i.text)
#     if (i.text=='Books'):
#         i.click()
#         break


# print(len(dropdownbox_xpath))
# for i in dropdownbox_xpath:
#     print(i.text)
#     if i.text=='Baby':
#         i.click()
#         break


time.sleep(5)
print(driver.title)
driver.close()
