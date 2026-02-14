import requests
from bs4 import BeautifulSoup
try:
    while True:
        print("\n")
        url = input("Введите ссылку:")
        print("\n")
        response = requests.get(url)
        i = response.status_code    
        if i == 200:
            print("Включен (статус код 200)")
        else:
            print("Выключен")
        main = BeautifulSoup(response.text, 'html.parser')

        div_count = len(main.find_all('div'))
        p_count = len(main.find_all('p'))
        a_count = len(main.find_all('a'))
        h1_count = len(main.find_all('h1'))
        img_count = len(main.find_all('img'))

        print("Всего тегов div (пустой тег почти для всего):", div_count)
        print("Всего тегов p (тег обычного текста):",p_count)
        print("Всего тегов a (ссылок):",a_count)
        print("Всего тегов h1 (заглавный тег):",h1_count)
        print("Всего тегов img (картинок):",img_count)
except:
    print("Введите правильную ссылку")
    while True:
        print("\n")
        url = input("Введите ссылку:")
        print("\n")
        response = requests.get(url)
        i = response.status_code    
        if i == 200:
            print("Включен (статус код 200)")
        else:
            print("Выключен")
        main = BeautifulSoup(response.text, 'html.parser')

        div_count = len(main.find_all('div'))
        p_count = len(main.find_all('p'))
        a_count = len(main.find_all('a'))
        h1_count = len(main.find_all('h1'))
        img_count = len(main.find_all('img'))

        print("Всего тегов div (пустой тег почти для всего):", div_count)
        print("Всего тегов p (тег обычного текста):",p_count)
        print("Всего тегов a (ссылок):",a_count)
        print("Всего тегов h1 (заглавный тег):",h1_count)
        print("Всего тегов img (картинок):",img_count)