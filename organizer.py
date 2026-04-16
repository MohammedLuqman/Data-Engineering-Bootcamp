import shutil
import pandas as pd
import os

df = pd.read_csv("./processed/cleaned_books.csv")

for star in range(1, 6):
    books = df[df['star_rating'] == star].copy()
    
    img_dir = f"./processed/images/{star}_star"
    csv_dir = f"./processed/{star}_star"
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(csv_dir, exist_ok=True)

    for i in range(len(books)):
        origin_path = books.iloc[i]['img_path']
        title = books.iloc[i]['title']
        
        if not os.path.exists(origin_path):
            origin_path = origin_path.replace("./images/", "./raw/images/")

        dest_path = f"{img_dir}/{title}.png"

        if os.path.exists(origin_path):
            shutil.copy(origin_path, dest_path)
            books.iloc[i, 3] = dest_path 

    books.to_csv(f"{csv_dir}/{star}_star_books.csv", index=False)