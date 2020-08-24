import requests
from bs4 import BeautifulSoup
import re

source = requests.get('https://en.wikipedia.org/wiki/Main_Page').text
soup = BeautifulSoup(source, 'lxml')

# pattern = re.compile(r'h[1-6]')
# res_h = soup.find_all(pattern)

res_h = soup.find_all(['h1', 'h2', 'h3'])

for head in res_h:
    print(head, end='\n\n')