# python3

import requests
# from bs4 import BeautifulSoup


def main():
    print("Input the URL:")
    link = input()
    response = requests.get(link)
    if response:
        file = open('source.html', 'wb')
        file.write(response.content)
        file.close()
        print("Content saved.")
    else:
        print("The URL returned %s!" % response.status_code)


main()
