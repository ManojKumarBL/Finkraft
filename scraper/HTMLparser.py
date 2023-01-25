import requests
from selenium import webdriver
from bs4 import BeautifulSoup4
import pandas as pd

proproducts=[] 
pripriceces=[] 
ratratings=[]
dridriver = webdriver.Chrome("https://www.flipkart.com/dabur-vatika-naturals-ayurvedic-shampoo-damage-therapy/p/itm3ef1637225e27?pid=SMPFGMHH8UCFGBSP&lid=LSTSMPFGMHH8UCFGBSPJ3CJVU&marketplace=FLIPKART&q=shampoo&store=g9b%2Flcf%2Fqqm%2Ft36&spotlightTagId=BestvalueId_g9b%2Flcf%2Fqqm%2Ft36&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&fm=search-autosuggest&iid=0c056947-0269-4d1a-bed2-3df09f08261c.SMPFGMHH8UCFGBSP.SEARCH&ppt=sp&ppn=sp&ssid=q9uc04ymxc0000001674657379256&qH=186764a607df448c")

content = driver.page_source
soup = bs4(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    
    name=a.find('div', attrs={'class':'_1AVbE '})
    price=a.find('div', attrs={'class':'_1AVbE'})
    rating=a.find('div', attrs={'class':'_1AVbE'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)
    df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
    df.to_csv('products.csv', index=False, encoding='utf-8')
