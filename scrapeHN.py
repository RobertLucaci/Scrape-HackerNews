import requests
from bs4 import BeautifulSoup
import pprint

links = []
subtexts = []


def get_data_from_pages():
    message = int(input('Hacker News\nNumber of pages you want to scrape: '))
    for page in range(1, message+1):
      res = requests.get(f'https://news.ycombinator.com/news?p={page}')
      soup = BeautifulSoup(res.text, 'html.parser')
      link = soup.select('.storylink')
      for i in link:
        links.append(i)
      subtext = soup.select('.subtext')
      for j in subtext:
        subtexts.append(j)


get_data_from_pages()


def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtexts):
    hn = []
    for idx, item in enumerate(links):
      title = item.getText()
      href = item.get('href', None)
      vote = subtexts[idx].select('.score')
      if len(vote):
        points = int(vote[0].getText().replace(' points', ''))
        if points > 99:
          hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtexts))
