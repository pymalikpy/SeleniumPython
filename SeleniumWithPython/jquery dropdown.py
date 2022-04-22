#single selection
#multi selection
# all selection
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

c = webdriver.ChromeOptions()
# incognito parameter passed
c.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=c)

def dropdown_list_value(options_list,value):
    if not value[0] == 'all':
        for i in drop_list:
            print(i.text)
            for k in range(len(value)):
                 if i.text == value[k]:
                    i.click()
                    break
    else:
        try:
            for i in options_list:
                i.click()
        except Exception as e:
            print(e)


driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
driver.implicitly_wait(2)
driver.find_element(By.ID, 'justAnInputBox').click()
time.sleep(2)
drop_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
#calling array of values from above method
values_list=['choice 2', 'choice 3', 'choice 6 2 1']
# values_list=['choice 7']
# values_list = ['all']
dropdown_list_value(drop_list , values_list)
# dropdown_list_value(drop_list, 'choice 2')
# dropdown_list_value(drop_list, 'choice 3')
# dropdown_list_value(drop_list, 'choice 6 2 1')
driver.close()

# for i in drop_list:
#     print(i.text)
#     if i.text == 'choice 6 2 3':
#         i.click()
#         break
