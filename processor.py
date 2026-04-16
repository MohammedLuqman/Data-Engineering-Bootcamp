from scraper import raw_books
import pandas as pd 
import os

df = pd.DataFrame(raw_books)

df['price'] = df['price'].str.replace('£', '', regex=False)
df['price'] = df['price'].str.replace('Â', '', regex=False)
df['price'] = df['price'].astype(float)

df['star_rating'] = df['star_rating'].map({
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
})

df['star_rating'] = df['star_rating'].astype('Int64')

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

df.to_csv("./processed/cleaned_books.csv", index=False) 
