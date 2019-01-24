import requests
from bs4 import BeautifulSoup

page_result = requests.get('https://en.wikipedia.org/wiki/Portal:History')
parse_obj = BeautifulSoup(page_result.content, 'html.parser')

h_obj = parse_obj.find(class_='hlist noprint')
h_obj_a_content = h_obj.find_all('a')

print(h_obj)
print(h_obj_a_content)

