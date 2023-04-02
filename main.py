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
        body = article.find('p').text
        if title == 'News':
            title = article.find('a', class_='c-card__link').text
            for i in title:
                if i in string.punctuation:
                    title = title.replace(i, '')
                elif i in string.whitespace:
                    title = title.replace(i, '_')
            items[title] = body
    print(items)
    return items

def write_data(items):
    for item in items:
        with open(f'{item}.txt', 'w', 'utf-8') as file:
            file.write(items[item])

def main():
    write_data(get_data())
    


main()
