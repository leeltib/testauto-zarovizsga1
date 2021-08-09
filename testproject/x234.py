# 1 Feladat: Keressük a téglalap kerületét

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get('https://black-moss-0a0440e03.azurestaticapps.net/x234.html')

# ------------------------------------------------------------------------------

# bevitelő mezők definiálása:
inp_a = driver.find_element_by_id('a')
inp_b = driver.find_element_by_id('b')
calc_but = driver.find_element_by_id('submit')
er = driver.find_element_by_id('result')


# függvény a mezők törléséhez
def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element


# függvény a tesztadatok beviteléhez és az értékeléshez
def test_calc(a, b, exp):
    find_and_clear_by_id("a").send_keys(a)
    find_and_clear_by_id("b").send_keys(b)
    calc_but.click()
    er = driver.find_element_by_id('result')
    get_res = er.text
    print(get_res)
    try:
        assert get_res == exp
        print("Teszt eredmény OK!")
    except:
        print("Error!")


# futtatás (tesztelés) a megadott tesztadatok alapján:
test_calc(99, 12, '222')
test_calc('kiskutya', 12, 'NaN')
test_calc('', '', 'NaN')

time.sleep(2)
driver.close()

