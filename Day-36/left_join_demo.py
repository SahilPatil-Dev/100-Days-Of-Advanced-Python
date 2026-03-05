import pandas as pd

# Products dataset
products = pd.DataFrame({
    "product_id": [1, 2, 3, 4],
    "product_name": ["Laptop", "Mouse", "Keyboard", "Monitor"]
})

# Sales dataset
sales = pd.DataFrame({
    "product_id": [1, 2, 2],
    "quantity": [5, 10, 3]
})

# Left join
merged = pd.merge(products, sales, on="product_id", how="left")

print(merged)