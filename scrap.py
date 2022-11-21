import requests
from bs4 import BeautifulSoup
import pandas as pd

tumyorumlar = []


def get_soup(url):
    r = requests.get('http://localhost:8050/render.html', params={'url': url})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


# yorumlar
def yorumlarial(soup):
    yorum = soup.find_all('div', {'class', 'review-container'})
    try:
        for item in yorum:
            yorum = (item.find('p', {'class': 'partial_entry'}).text.strip())
            tumyorumlar.append(yorum)
    except:
        pass


# sonraki sayfa
for x in range(0, 15800, 15):
    soup = get_soup(
        f'https://www.tripadvisor.co.uk/Restaurant_Review-g186338-d4495284-Reviews-or{x}-Aqua_Shard-London_England.html')
    yorumlarial(soup)
    print(len(tumyorumlar))
    if not soup.find('div', {'class': 'nav next ui_button primary'}):
        pass
    else:
        break

df = pd.DataFrame(tumyorumlar)
df.to_csv('reviews.csv')
print('bitti')
