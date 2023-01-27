import pandas as pd
import requests
from bs4 import BeautifulSoup4

# URL
url = "https://www.flipkart.com/biotique-ocean-kelp-anti-hair-fall-shampoo-650ml/p/itma722af8f7d1ea?pid=SMPFKXTYD4FWWPHW&lid=LSTSMPFKXTYD4FWWPHWSIYQBK&marketplace=FLIPKART&q=shampoo&store=g9b%2Flcf%2Fqqm%2Ft36&srno=s_1_5&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&fm=search-autosuggest&iid=3fbce9cb-6319-47b3-8445-036d907c7258.SMPFKXTYD4FWWPHW.SEARCH&ppt=sp&ppn=sp&ssid=237nv10dls0000001674803406570&qH=186764a607df448c"
df = pd.read_excel(r'Path where the Excel file is stored\File name.xlsx')


response = requests.get(url)
html_content = response.text

soup = BeautifulSoup4(html_content, "html.parser")


product_elements = soup.find_all("div", class_="_1AtVbe")

product_list=[]
for product_element in product_elements:
    name = product_element.find("h3").text
    price = product_element.find("span", class_="price").text
    description = product_element.find("p", class_="description").text
    image_url = product_element.find("img")["src"]

    product_list.append([name,price,image_url])
    data_frame=pd.DataFrame(product_list)
    writer = pd.ExcelWriter(df, engine='xlsxwriter')
    data_frame.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()