import requests
from bs4 import BeautifulSoup
import random2

# from googletrans import Translator
from googletrans import Translator

def get_words():
    response = requests.get('https://englishvocabs.com/vocabulary/1000-most-common-english-words-and-meaning/')
    soup = BeautifulSoup(response.text, 'html.parser')



    words = []
    for i in soup.findAll('tr')[1:]:
        word = i.findAll('td')[0].text
        meaning = i.findAll('td')[1].text
        words.append((word, meaning))


    return words
# Создаем экземпляр класса

trans = Translator()



def game_words():
    words = get_words()
    while True:
        k = random2.randint(0, len(words) - 1)
        print('Слово: ', words[k][0])
        word = words.pop(k)

        print(word[1], Translator().translate(word[1], src='en', dest='ru').text)

        answer = input('Ваш ответ: ')
        if answer == word[0]:
            print('Верно')
        else:
            print('Неверно')
            print('Правильный ответ: ', word[0])

        continue_game = input('Продолжить? (y/n) ')
        if continue_game == 'y':
            continue
        else:
            break

# Переводим текст


# Выводим результат
game_words()