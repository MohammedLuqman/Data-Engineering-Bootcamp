import os

os.makedirs("./raw/images", exist_ok=True)
os.makedirs("./processed", exist_ok=True)

print("Scraping the website")
os.system("python scraper.py")

print("Processing data")
os.system("python processor.py")

print("Organizing data")
os.system("python organizer.py")

print("Done All")