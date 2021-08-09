# 5 Feladat: Kakukktojás - városok

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get('https://black-moss-0a0440e03.azurestaticapps.net/rv4.html')

# ------------------------------------------------------------------------------

# a textarea tartalmának listába gyűjtése:
area_cities = driver.find_element_by_id('cites').get_attribute('value')
cities_list = area_cities.replace('"', '').replace(' ', '').split(',')
print(cities_list)
print(len(cities_list))


# a felsorolt városok listába gyűjtése:
li_cities = driver.find_elements_by_tag_name('li')
list_li_cities = []
for city in li_cities:
    city_name = city.text.replace(" ", "")
    list_li_cities.append(city_name)

print(list_li_cities)
print(len(list_li_cities))


# a két lista összehasonlítása, a hiányzó város kiírása:
mis_city = ''
for ci in cities_list:
    if ci in list_li_cities:
        pass
    else:
        mis_city += ci

print(mis_city)

# ellenörzés:
inp_contr = driver.find_element_by_id('missingCity')
but_contr = driver.find_element_by_id('submit')

inp_contr.send_keys(mis_city)
but_contr.click()

res_contr = driver.find_element_by_id('result')

try:
    assert res_contr == "Nem találtad el."
    print("Nem találtad el!")
except:
    print("Gratulálok! Eltaláltad a hiányzó város nevét.")
finally:
    time.sleep(2)
    driver.close()


