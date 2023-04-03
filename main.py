# python3

import requests
from bs4 import BeautifulSoup
import string

page = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'


def get_data():
    response = requests.get(page)
    items = {}
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        title = article.find('span', class_='c-meta__type').text
        body_link= article.find('div', class_='c-card__link u-link-inherit').text
        testing = article
        if title == 'News':
            title = article.find('a', class_='c-card__link').text
            for i in title:
                if i in string.punctuation:
                    title = title.replace(i, '')
                elif i in string.whitespace:
                    title = title.replace(i, '_')
            items[title] = body_link
    print(testing)
    return items

def write_data(items):
    for item in items:
        response = requests.get(items[item])
        soup = BeautifulSoup(response.text, 'html.parser')
        body = soup.find('p', class_='article__teaser')
        file = open(f'{str(item)}.txt', 'wb')
        file.write(str(body).encode())
        file.close()

def main():
    get_data()


main()
