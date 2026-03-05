import pandas as pd

# Users dataset
users = pd.DataFrame({
    "user_id": [1, 2, 3],
    "name": ["Sahil", "Amit", "Neha"]
})

# Orders dataset
orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "user_id": [1, 2, 1, 3],
    "amount": [500, 700, 300, 900]
})

# Merge datasets
merged = pd.merge(orders, users, on="user_id", how="inner")

print("Orders with user names:")
print(merged)

# Total order amount per user
revenue_per_user = (
    merged.groupby("name")["amount"]
    .sum()
    .reset_index()
    .sort_values(by="amount", ascending=False)
)

print("\nTotal revenue per user:")
print(revenue_per_user)