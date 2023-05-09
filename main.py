from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from auth_data import password, login

url = 'http://nz.ua'

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/112.0.0.0")
s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
  '''
})


try:
    driver.get(url=url)
    time.sleep(1)


    login_input = driver.find_element(By.ID, 'loginform-login')
    login_input.clear()
    login_input.send_keys(login)
    time.sleep(5)

    password_input = driver.find_element(By.ID, 'loginform-password')
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(5)

    continiue = driver.find_element(By.LINK_TEXT, 'Увійти')
    continiue.click()
    time.sleep(15)

    input_cloudfare = driver.find_element(By.XPATH, '//*[@id="challenge-stage"]/div/label/input')
    input_cloudfare.click()
    time.sleep(10)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()