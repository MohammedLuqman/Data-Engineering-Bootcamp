from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import os
import pandas as pd

os.makedirs("./raw/images", exist_ok=True)
raw_books = []
current_page = 1

url = f"https://books.toscrape.com/catalogue/page-{current_page}.html"

while current_page and current_page < 4 :
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text , "html.parser")
    
    articles = soup.find_all("article", class_ = "product_pod")
    for article in articles:
        title = article.h3.a["title"][:50].replace(":", "",).replace("/", "").replace("?", "").replace(".", "")
        price = article.find("p", class_="price_color").text 
        star_rating = article.find('p', class_ = 'star-rating')['class'][1]
        img_src = urljoin(url ,article.find("img")["src"])
        
        img_path =  requests.get(img_src)
        with open (f"./raw/images/{title}.png", "wb") as img:
            img.write(img_path.content)
            
        raw_books.append({
            "title": title,
            "price": price,
            "star_rating": star_rating,
            "img_path": f"./images/{title}.png",
        })
    
    next = soup.find("li", class_="next")
    if next :
        current_page +=1
        url = f"https://books.toscrape.com/catalogue/page-{current_page}.html"
    else : 
        break 

df = pd.DataFrame(raw_books)
df.to_csv("./raw/raw_books.csv", index=True)