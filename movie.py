import requests
from bs4 import BeautifulSoup 
response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
soup = BeautifulSoup(response.text, 'html.parser')
titles=soup.find_all('h3',class_='title')
titles = titles[::-1]
for title in titles:
    print(title.text)