import requests
from bs4 import BeautifulSoup

# URL 
url = "https://www.flipkart.com/dabur-vatika-naturals-ayurvedic-shampoo-damage-therapy/p/itm3ef1637225e27?pid=SMPFGMHH8UCFGBSP&lid=LSTSMPFGMHH8UCFGBSPJ3CJVU&marketplace=FLIPKART&q=shampoo&store=g9b%2Flcf%2Fqqm%2Ft36&spotlightTagId=BestvalueId_g9b%2Flcf%2Fqqm%2Ft36&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&fm=search-autosuggest&iid=0c056947-0269-4d1a-bed2-3df09f08261c.SMPFGMHH8UCFGBSP.SEARCH&ppt=sp&ppn=sp&ssid=q9uc04ymxc0000001674657379256&qH=186764a607df448c"


response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")


product_elements = soup.find_all("div", class_="product")

for product_element in product_elements:
        name = product_element.find("h3").text
        price = product_element.find("span", class_="price").text
        description = product_element.find("p", class_="description").text
        image_url = product_element.find("img")["src"]
        print(f"Name: {name}")
        print(f"Price: {price}")
        print(f"Description: {description}")
        print(f"Image URL: {image_url}")
