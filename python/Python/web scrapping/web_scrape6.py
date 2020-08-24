import sys, re
import requests
from bs4 import BeautifulSoup

source = requests.get('https://en.wikipedia.org/wiki/Python').text

soup = BeautifulSoup(source, 'lxml')

res_body = soup(text=re.compile(r'Python'))
for el in res_body:
    print(el.parent)
