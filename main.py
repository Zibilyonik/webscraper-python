# python3
import requests


def main():
    print("Input the URL:")
    link = input()
    response = requests.get(link)
    try:
        print(response.json()['content'])
    except KeyError:
        print("Invalid quote resource")


main()
