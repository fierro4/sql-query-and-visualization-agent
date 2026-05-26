import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

files = {
    "customers": "data/olist_customers_dataset.csv",
    "orders": "data/olist_orders_dataset.csv",
    "order_items": "data/olist_order_items_dataset.csv",
    "products": "data/olist_products_dataset.csv",
    "order_payments": "data/olist_order_payments_dataset.csv",
    "order_reviews": "data/olist_order_reviews_dataset.csv"
}

for table, file in files.items():
    print(f"Loading {table}...")
    df = pd.read_csv(file)
    df.to_sql(table, conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully.")