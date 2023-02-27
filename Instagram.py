import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup as BS
import Auth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import datetime

def get_source_html():
    service = Service(executable_path="D:\\Instagram\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    # Меняем user-agent в ручном режиме
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15")
    # Отключение режима вебдрайвера
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Добавление новых аргументов для изменения user-agent и отключения режима вебдрайвера
    driver = webdriver.Chrome(service=service, options=options)
    # Ростянуть окно на весь экран
    driver.maximize_window()
    try:
        # Добавляем счетчик времени исполнения скрипта
        start_time = datetime.datetime.now()
        # Заходим на сайт инстаграма
        driver.get("https://www.instagram.com/")
        driver.implicitly_wait(1)
        # time.sleep(1)
        # Авторизация
        text_box = driver.find_element(by=By.NAME, value="username")
        text_box.clear()
        text_box.send_keys(Auth.username)
        time.sleep(4)
        # driver.implicitly_wait(1)
        text_box = driver.find_element(by=By.NAME, value="password")
        text_box.clear()
        text_box.send_keys(Auth.password + Keys.ENTER)
        time.sleep(4)
        # driver.implicitly_wait(3)
        # закрытие всплывающих уведомлений
        driver.execute_script("document.getElementsByClassName('_acan _acao _acas')[0].click()")
        time.sleep(3)
        # driver.implicitly_wait(3)
        driver.execute_script("document.getElementsByClassName('_a9-- _a9_1')[0].click()")
        time.sleep(3)
        # driver.implicitly_wait(3)
        # Клик на мою страницу
        # driver.execute_script("document.getElementsByClassName('x6umtig x1b1mbwd xaqea5y xav7gou xk390pu')[0].click()")
        # time.sleep(4)
        # открываем посковик профилей
        driver.execute_script("document.getElementsByClassName('x9f619 xxk0z11 xvy4d1p')[1].click()")
        time.sleep(3)
        # driver.implicitly_wait(3)
        # вводим данные для поиска
        text_box = driver.find_element(By.CLASS_NAME, "_aauy")
        text_box.clear()
        text_box.send_keys(Auth.user_0)
        time.sleep(3)
        # driver.implicitly_wait(3)
        # Нажимаем на искомый профиль
        driver.execute_script("document.getElementsByClassName('_ab8w  _ab94 _ab97 _ab9f')[0].click()")
        time.sleep(3)
        # driver.implicitly_wait(3)
        # Дописываем счетчик времени исполнения скрипта и выводим результат в консоль
        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time
        print(spent_time)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


get_source_html()
