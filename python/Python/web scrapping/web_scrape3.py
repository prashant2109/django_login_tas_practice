from bs4 import BeautifulSoup
import requests
source  = requests.get('https://www.data.gov/').text

soup = BeautifulSoup(source, 'lxml')
res_div  = soup.find('div', class_='getstarted')
print(res_div.h4.small.a.text)
