import requests
from bs4 import BeautifulSoup

page_result = requests.get('https://www.imdb.com/news/top?ref_=nv_nw_tp')
parse_obj = BeautifulSoup(page_result.content, 'html.parser')

top_news = parse_obj.find(class_='news-article__content')
top_news_a_content = top_news.find_all('a')

print(top_news_a_content)

