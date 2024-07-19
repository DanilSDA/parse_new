# Задание 1: Получение данных
#
# Импортируйте библиотеку requests.
#
# Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром для поиска репозиториев с кодом html.
#
# Распечатайте статус-код ответа.
#
# Распечатайте содержимое ответа в формате JSON.

import requests
from pprint import pprint




print( 'Задание 1' )
response = requests.get('https://api.github.com/search/repositories?q=language:html')
print(response.status_code)
pprint(response.json())

#
# Задание 2: Параметры запроса
#
# Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
#
# Отправьте GET-запрос с параметром userId, равным 1.
#
print( 'Задание 2' )

param = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=param)
if response.status_code == 200:

    for i in response.json():
        pprint(i)
else:
    print('Ошибка')
#pprint(response.json())


#
#
# Задание 3: Отправка данных
#
# Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
#
# Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
#
# Отправьте POST-запрос с этими данными.
#
# Распечатайте статус-код и содержимое ответа.
#
#
print( 'Задание 3' )

response = requests.post('https://jsonplaceholder.typicode.com/posts', data={'title': 'foo', 'body': 'bar', 'userId': 1})
print(response.status_code)
pprint(response.json())