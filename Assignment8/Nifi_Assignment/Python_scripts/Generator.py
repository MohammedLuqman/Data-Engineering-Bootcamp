import random
import time
from datetime import datetime
import psycopg2

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": "5432",
    "database": "orders_db",
    "user": "admin",
    "password": "admin"
}

def setup_database():
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id SERIAL PRIMARY KEY,
            order_id INT,
            customer_name TEXT,
            product TEXT,
            price TEXT,
            quantity INT,
            city TEXT,
            order_date TEXT
        )
    """)
    conn.commit()
    return conn, cursor

names = ["Ali Ahmed", "Sara Ali", "Omar Hassan", None]
products = ["Laptop", "Phone", "Tablet", "Headphones"]
cities = ["Taiz", "Sana'a", "Aden", None]

try:
    conn, cursor = setup_database()
    print("Connected! Generating and inserting orders...")

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

        insert_query = """
        INSERT INTO orders (order_id, customer_name, product, price, quantity, city, order_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(insert_query, (
            order["order_id"],
            order["customer_name"],
            order["product"],
            str(order["price"]) if order["price"] is not None else None,
            order["quantity"],
            order["city"],
            order["order_date"]
        ))

        conn.commit()
        print(f"Successfully Inserted: {order['order_id']} - {order['customer_name']}")
        time.sleep(3)

except Exception as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nStopping script...")
finally:
    if 'cursor' in locals(): cursor.close()
    if 'conn' in locals(): conn.close()