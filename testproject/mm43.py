# 4 Feladat: Email mező

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get('https://black-moss-0a0440e03.azurestaticapps.net/mm43.html')

# ------------------------------------------------------------------------------

# bevitelő mezők definiálása:
inp_email = driver.find_element_by_id('email')
subm_but = driver.find_element_by_id('submit')


# függvény a mezők törléséhez
def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element


# függvény a tesztadatok beviteléhez és az értékeléshez
def test_calc(mail, exp, exp_b):
    find_and_clear_by_id("email").send_keys(mail)
    subm_but.click()
    val = driver.find_elements_by_class_name('validation-error')
    print('-' * 20)
    if len(val) > 0:
        get_res = val[0].text
        print(get_res)
    else:
        get_res = ""
    try:
        assert get_res == exp or get_res == exp_b
        print("Teszt eredmény OK!")
    except:
        print("Error!")


# futtatás (tesztelés) a megadott tesztadatok alapján:

mail1 = 'teszt@elek.hu'
exp1 = ""
exp1b = ""
test_calc(mail1, exp1, exp1b)

mail2 = 'teszt@'
exp2 = 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.'
exp2b = "Please enter a part following '@'. 'teszt@' is incomplete."
test_calc(mail2, exp2, exp2b)

mail3 = ""
exp3 = "Kérjük, töltse ki ezt a mezőt."
exp3b = "Please fill out this field."
test_calc(mail3, exp3, exp3b)


time.sleep(2)
driver.close()



