import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

bookUrl = 'https://books.toscrape.com/'
bookHeader = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
Data = rq.get(url=bookUrl, headers=bookHeader)
Soup = BeautifulSoup(Data.content, 'html.parser')
# print(bookSoup)
Names = Soup.find_all('h3')
book1 = [i.text for i in Names]
bDataframe = pd.DataFrame(book1,columns=['Book Name'])
bDataframe.to_csv('Book2.csv')
