# python3

import requests
from bs4 import BeautifulSoup

def main():
    web_dict={}
    while True:
        link = input("Input the URL:")
        if link.find("nature.com/articles") != -1:
            break
        print("Invalid page!")
    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")
        if soup.find("title").text:
            web_dict["title"] = soup.find("title").text
            web_dict["description"] = soup.findAll("meta", {"name": "description"})[0]["content"]
    except KeyError:
        print("Invalid quote resource")
    else:
        print(web_dict)


main()
