import requests
from bs4 import BeautifulSoup
from .database import SessionLocal, engine 
from .models import Quote, Base


def scrape_and_store():
    raw_quotes = []

    for current_page in range(1, 11):
        print(f"Scraping page {current_page}...")
        
        url = f"https://quotes.toscrape.com/page/{current_page}/"
        webpage_link = requests.get(url)
        soup = BeautifulSoup(webpage_link.content, 'html.parser')

        quote_divs = soup.find_all('div', class_="quote")

        for q in quote_divs:
            text = q.find('span', class_="text").text
            author = q.find('small', class_="author").text
            tags = q.find_all('a', class_="tag")
            tag_list = [t.text for t in tags]
            tags_string = ", ".join(tag_list)
            
            raw_quotes.append({
                "Quote": text,
                "Author": author,
                "Tags": tags_string
            })

    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        print("Saving to DB...")

        for q in raw_quotes:
            exists = db.query(Quote).filter(Quote.quote == q["Quote"]).first()
            
            if not exists:
                new_quote = Quote(
                    quote=q["Quote"],
                    author=q["Author"],
                    tags=q["Tags"]
                )
                db.add(new_quote)

        db.commit()
        print("Done!")

    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()