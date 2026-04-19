"""
generate_data.py
Generates sample raw sales CSV data with intentional dirty data for ETL demo.
"""

import pandas as pd
import numpy as np
import os
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

def generate_raw_sales(n=200):
    products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard", None]
    regions  = ["North", "South", "East", "West", None]

    start = datetime(2024, 1, 1)
    records = []

    for i in range(1, n + 1):
        sale_date = start + timedelta(days=random.randint(0, 364))
        qty = random.choice([random.randint(1, 20), None])  # some nulls
        price = round(random.uniform(50, 2000), 2)

        records.append({
            "sale_id":   i,
            "product":   random.choice(products),
            "region":    random.choice(regions),
            "sale_date": sale_date.strftime("%Y-%m-%d") if random.random() > 0.05 else "invalid-date",
            "quantity":  qty,
            "unit_price": price,
        })

    # Add deliberate duplicates
    for _ in range(10):
        records.append(random.choice(records))

    df = pd.DataFrame(records)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_sales.csv", index=False)
    print(f"✅ Generated {len(df)} raw sales records → data/raw_sales.csv")

if __name__ == "__main__":
    generate_raw_sales()
