# 2 Feladat: Pénzfeldobás

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get('https://black-moss-0a0440e03.azurestaticapps.net/tts4.html')

# ------------------------------------------------------------------------------

# felhasznált elemek definiálása:
sub_button = driver.find_element_by_id('submit')

# megszámoljuk, hogy 100 esetből hányszor lesz 'fej' az eredmény:
num_f = 0
for i in range(100):
    sub_button.click()
    time.sleep(0.1)
    result_car = driver.find_element_by_id('lastResult').text
    if result_car == 'fej':
        num_f += 1
    else:
        pass

print(num_f)

# az eredmény értékelése:
try:
    assert num_f >= 30
    print('Eredmény OK!')
except:
    print('Rossz eredmény, 30-nál kevesebb a "fej"!')
finally:
    time.sleep(2)
    driver.close()



