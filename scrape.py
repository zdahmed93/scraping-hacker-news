import requests
from bs4 import BeautifulSoup
import pprint

pages = 3

all_links = []
all_subtexts = []

for i in range(1, pages+1):
    print(i)
    web_page_url = f'https://news.ycombinator.com/news?p={str(i)}'
    print(web_page_url)
    res = requests.get(web_page_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.storylink')
    subtexts = soup.select('.subtext')
    all_links.extend(links)
    all_subtexts.extend(subtexts)


def filter_news(links, subtexts):
    filtered_news = []
    for index, item in enumerate(links):
        title = links[index].getText()
        link = links[index].get('href')
        score = subtexts[index].select('.score')
        if len(score):
            votes = int(score[0].getText().replace(' points', ''))
            if (votes >= 100):
                filtered_news.append({
                    'title': title,
                    'link': link,
                    'score': votes
                })
    return sorted(filtered_news, key=lambda k: k['score'], reverse=True)


pprint.pprint(filter_news(all_links, all_subtexts))
