import csv
import time
import random
import uuid
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
DATA_DIR = os.path.join(BASE_DIR, "ecommerce_data")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

COLUMNS = ["order_id", "timestamp", "customer_id", "product_name", "category", "price", "quantity", "payment_method"]

PRODUCTS = {
    "Electronics": ["Laptop", "Smartphone", "Wireless Mouse", "Monitor"],
    "Fashion": ["Running Shoes", "T-Shirt", "Jacket"],
    "Home": ["Coffee Maker", "Desk Lamp", "Air Purifier"]
}

PAYMENT_METHODS = ["Credit Card", "PayPal", "Cash", "Crypto"]
TIME_FORMATS = ["%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M", "UNIX_STAMP"]

def generate_messy_order():
    if random.random() < 0.05:
        return ["INVALID_ORDER", "00-00-00", "???", "NONE", "NONE", "ERROR", "0", "UNKNOWN"]

    order_id = f"ORD-{str(uuid.uuid4())[:8].upper()}"
    
    fmt = random.choice(TIME_FORMATS)
    timestamp = str(int(time.time())) if fmt == "UNIX_STAMP" else datetime.now().strftime(fmt)
    
    category = random.choice(list(PRODUCTS.keys()))
    product = random.choice(PRODUCTS[category])
    
    price = round(random.uniform(5.0, 1200.0), 2)
    if random.random() < 0.08: price = price * -1 
    if random.random() < 0.05: price = "FREE"    

    quantity = random.randint(1, 10)
    customer_id = f"USER_{random.randint(1000, 9999)}"

    row = [order_id, timestamp, customer_id, product, category, price, quantity, random.choice(PAYMENT_METHODS)]
    
    # (Missing values) 
    if random.random() < 0.1:
        row[random.randint(0, len(row)-1)] = ""
        
    return row

def start_order_stream():
    print(f"Generator is running")
    batch_size = 30 

    try:
        while True:
            batch_data = []
            for _ in range(batch_size):
                batch_data.append(generate_messy_order())
            
            batch_id = str(uuid.uuid4())[:8].upper()
            file_name = f"batch_{batch_id}.csv"
            file_path = os.path.join(DATA_DIR, file_name)

            with open(file_path, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
                writer.writerow(COLUMNS) 
                writer.writerows(batch_data) 

            print(f"Saved {file_name} with {batch_size} orders.")

            if random.random() < 0.05:
                dup_path = os.path.join(DATA_DIR, f"copy_{file_name}")
                with open(dup_path, mode='w', newline='', encoding='utf-8') as df:
                    writer = csv.writer(df, quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(COLUMNS)
                    writer.writerows(batch_data)
                print(f"Sent twice!")

            time.sleep(2.0) 
            
    except KeyboardInterrupt:
        print("\n stopped.")

if __name__ == "__main__":
    start_order_stream()