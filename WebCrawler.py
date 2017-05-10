import requests
from bs4 import BeautifulSoup

def forum_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://thenewboston.com/forum/recent_activity.php?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'title'}):
            href = link.get('href')
            title = link.string
            get_single_item_data(href)
            # print(href + " " + title)
        for link in soup.findAll('a', {'class': 'user-name'}):
            href = link.get('href')
            username = link.string
            print(href + " " + username)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll('h1', {'class': 'forum-title'}):
        print(item_name.string)


forum_spider(5)