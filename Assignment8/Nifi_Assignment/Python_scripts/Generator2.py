import json
import random
import time
from datetime import datetime
import os

output_dir = r"C:\nifi-data"

os.makedirs(output_dir, exist_ok=True)

names = ["Ali Ahmed", "Sara Ali", "Omar Hassan", None]
products = ["Laptop", "Phone", "Tablet", "Headphones"]
cities = ["Taiz", "Sana'a", "Aden", None]

print(f"Generating orders in: {output_dir}")

try:
    while True:
        order = {
            "order_id": random.randint(1000, 1100),
            "customer_name": random.choice(names),
            "product": random.choice(products),
            "price": random.choice([100, 200, "300", None]),
            "quantity": random.randint(1, 3),
            "city": random.choice(cities),
            "order_date": random.choice([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                datetime.now().strftime("%d/%m/%Y"),
            ])
        }

        filename = os.path.join(
            output_dir,
            f"order_{int(time.time() * 1000)}.json"
        )

        with open(filename, "w") as f:
            json.dump(order, f, indent=4)

        print(f"Saved: {filename}")

        # Generate file every 3 seconds
        time.sleep(3)

except KeyboardInterrupt:
    print("\nStopping the script...")