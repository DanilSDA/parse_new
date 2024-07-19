from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def search_wikipedia(search_query):
    browser.get('https://ru.wikipedia.org/wiki/Main_Page')
    time.sleep(2)
    search_box = browser.find_element(By.ID, 'searchInput')
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

def list_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, 'p')
    for paragraph in paragraphs:
        print(paragraph.text)
    print("\n--- Конец статьи ---\n")

def choose_action():
    print("Выберите действие:")
    print("1 - Листать параграфы текущей статьи")
    print("2 - Перейти на одну из связанных страниц")
    print("3 - Выйти из программы")
    choice = input()
    return choice

def go_to_linked_page():
    links = browser.find_elements(By.CSS_SELECTOR, 'p a')
    if links:
        print(f"Переход на связанную страницу: {links[0].get_attribute('href')}")
        browser.get(links[0].get_attribute('href'))
        time.sleep(5)
    else:
        print("Связанные страницы не найдены.")

browser = webdriver.Chrome()

initial_query = input("Введите ваш запрос: ")
search_wikipedia(initial_query)

while True:
    action = choose_action()
    if action == '1':
        list_paragraphs()
    elif action == '2':
        go_to_linked_page()
    elif action == '3':
        print("Выход из программы.")
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")

browser.quit()