import requests
from bs4 import BeautifulSoup
import pandas as pd


for i in range(1,51):
    url = f'https://books.toscrape.com/catalogue/page-{1}.html'
    response = requests.get(url)    
    soup = BeautifulSoup(response.text, 'html.parser')
    ol = soup.find('ol')
    articles = soup.find_all('article', class_='product_pod')
    books = []


    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star = star['class'][1]
        price = article.find('p', class_='price_color').text
        price = float(price[2:])
        books.append([title, price, star])


    
df = pd.DataFrame(books, columns=['Title','Price','Star Rataing'])
df.to_csv('books.csv')
