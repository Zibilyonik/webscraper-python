# python3

import requests
from bs4 import BeautifulSoup
import string
import os


def get_data(page, article_type):
    response = requests.get('https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=' + str(page))
    items = {}
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        title = article.find('span', class_='c-meta__type').text
        body_link= article.find('a', class_='c-card__link u-link-inherit')['href']
        if title == str(article_type):
            title = article.find('a', class_='c-card__link').text
            for i in title:
                if i in string.punctuation:
                    title = title.replace(i, '')
                elif i in string.whitespace:
                    title = title.replace(i, '_')
            items[title] = body_link
    return items

def write_data(page, items):
    os.mkdir(f'Page_{page}')
    os.chdir(f'Page_{page}')
    for item in items:
        response = requests.get(f'https://www.nature.com{items[item]}')
        soup = BeautifulSoup(response.text, 'html.parser')
        body = soup.find('p', class_='article__teaser').text
        file = open(f'{str(item)}.txt', 'wb')
        file.write(str(body).encode())
        file.close()
    os.chdir('..')

#this function loops through the pages and calls the get_data function
def get_pages(pages, article_type):
    for i in range(1, int(pages)+1):
        write_data(i, get_data(i, article_type))

def main():
    pages = input()
    article_type = input()
    get_pages(int(pages), article_type)


main()
