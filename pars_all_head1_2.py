# Задача 4.2: Извлечение заголовков с веб-страницы
# Используйте BeautifulSoup для извлечения всех заголовков (тегов <h1>, <h2>, и т.д.) с веб-страницы. Инструменты: requests, BeautifulSoup Методы: requests.get(), BeautifulSoup(), find_all()
from pprint import  pprint
import requests
from bs4 import BeautifulSoup

url = 'https://lenta.ru/articles/2024/06/21/business/'
#url = "http://quotes.toscrape.com/"

response = requests.get(url)
print(response.status_code)

if response.status_code != 200:
    print('Error')



html = response.text

pprint(html)


soup = BeautifulSoup(response.text, 'html.parser')
for i in soup.find_all('span', class_="topic-body__title uwoiat"):
    print(i.text)

  # price = int([k if isint(k) in card_price].join(''))