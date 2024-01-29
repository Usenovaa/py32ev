'''
Веб скрейпинг -> технология получения данных из веб-сайтов

Парсинг -> анализ HTML кода и извлечение нужных данных (автоматическое, с возможностью записи в файл или бд)

1. отправляем запрос и получаем HTML код
2. html -> переводим в soup и вытаскивыем нужные теги
3. запись в файл
'''

import requests
from bs4 import BeautifulSoup as bs
import csv


def write_to_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price'], data['img']])


def get_html(url):
    response = requests.get(url)
    return response.text


def get_total_page(html):
    soup = bs(html, 'lxml')
    page = soup.find('li', class_='pagination-end').find('a').get('href')
    # print(page)
    page = page.split('-')[-1]
    return page


def get_data(html):
    soup = bs(html, 'lxml')
    # print(soup)
    product_list = soup.find_all('div', class_='row')
    # print(product_list)
    for product in product_list:
        title = product.find('div', class_='rows').find('a').text

        price = product.find('span', class_='price').text

        img = product.find('img').get('src')
        img = 'https://enter.kg'+img

        data = {
            'title': title,
            'price': price,
            'img': img
        }
        write_to_csv(data)


def main():
    url = 'https://enter.kg/computers/noutbuki_bishkek'
    html = get_html(url)
    pages = get_total_page(html)
    get_data(html)
    for i in range(100, int(pages)+1, 100):
        url = f'https://enter.kg/computers/noutbuki_bishkek/results,{i+1}-{i}'
        # print(url)
        html = get_html(url)
        get_data(html)


with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'price', 'image'])

main()

