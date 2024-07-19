from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#import re
#import pandas as pd
#import numpy as n

browser = webdriver.Chrome()

#browser.get
browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
time.sleep(5)
zapros = r'программирование' # input('Что ищем? ')

browser.find_element(By.ID ,'searchInput').send_keys(zapros)
time.sleep(2)
browser.find_element(By.ID ,'searchInput').send_keys(Keys.ENTER)
time.sleep(15)
paragraphs = browser.find_elements(By.TAG_NAME ,'p')
for paragraph in paragraphs:
    print(paragraph.text) 