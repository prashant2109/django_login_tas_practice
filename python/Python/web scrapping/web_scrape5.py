import requests
from bs4 import BeautifulSoup

source = requests.get('https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)').text

soup = BeautifulSoup(source, 'lxml')

res_img_lst = soup.find_all('img')
all_img_links = [img['src'] for img in res_img_lst]
print(all_img_links)