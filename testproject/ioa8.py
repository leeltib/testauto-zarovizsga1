# 3 Feladat: Összeadó

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get('https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html')

# ------------------------------------------------------------------------------

# felhasznált elemek definiálása:
num_1 = int(driver.find_element_by_id('num1').text)
oper = driver.find_element_by_id('op').text
num_2 = int(driver.find_element_by_id('num2').text)

calc_but = driver.find_element_by_id('submit')


# függvény a python által számolt értékhez:
def calc_py(n1, op, n2):
    if op == '+':
        num_calc_py = n1 + n2
        return num_calc_py
    elif op == '-':
        num_calc_py = n1 - n2
        return num_calc_py
    elif op == '*':
        num_calc_py = n1 * n2
        return num_calc_py
    elif op == '/':
        num_calc_py = n1 / n2
        return num_calc_py
    elif op == '//':
        num_calc_py = n1 // n2
        return num_calc_py
    elif op == '**':
        num_calc_py = n1 ** n2
        return num_calc_py
    elif op == '%':
        num_calc_py = n1 % n2
        return num_calc_py
    else:
        print("Ismeretlen operátor jel!")


# futtatás, eredmény értékelés:
num_ca_py = calc_py(num_1, oper, num_2)
print(num_ca_py)
calc_but.click()
num_res = int(driver.find_element_by_id('result').text)
print(num_res)

try:
    assert num_ca_py == num_res
    print("Eredmény OK!")
except:
    print("A két eredmény nem azonos!")
finally:
    time.sleep(2)
    driver.close()


