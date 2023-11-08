import requests
from bs4 import BeautifulSoup
import json

url = 'https://schyolkovo.spim.ru/shop/matras/?sort=popularity&layout=tile&idtype=5&sizes_w=0&sizes_d=0'

# Получение содержимого страницы
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Извлечение информации из различных тегов с заданными классами
    items = soup.find_all('div', class_='good-item')

    data = []

    for item in items:
        name = item.find('div', class_='good-name').get_text().strip()
        price = item.find('span', class_='price-val').get_text().strip()
        size = item.find('div', class_='good-param good-size-param').get_text().strip()
        hardness = item.find('div', class_='good-params').get_text().strip()
        description = item.find('div', class_='good-item-hover-params').get_text().strip()

        data.append({
            'Наименование': name,
            'Цена': price,
            'Размер': size,
            'Жесткость': hardness,
            'Описание': description
        })

    # Сохранение в формате JSON
    with open('parsed_data1.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
else:
    print("Ошибка при получении страницы")