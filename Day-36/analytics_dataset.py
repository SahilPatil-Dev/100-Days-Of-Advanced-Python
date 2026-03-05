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

# Payments dataset
payments = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "payment_method": ["card", "upi", "card", "upi"]
})

# Merge orders with users
orders_users = pd.merge(orders, users, on="user_id", how="inner")

# Merge payments
full_dataset = pd.merge(orders_users, payments, on="order_id", how="inner")

print("Combined analytics dataset:")
print(full_dataset)

# Total revenue per user
revenue_per_user = (
    full_dataset.groupby("name")["amount"]
    .sum()
    .reset_index()
)

# Number of orders per user
orders_per_user = (
    full_dataset.groupby("name")["order_id"]
    .count()
    .reset_index(name="order_count")
)

# Average order value
avg_order_value = (
    full_dataset.groupby("name")["amount"]
    .mean()
    .reset_index(name="avg_order_value")
)

print("\nRevenue per user:")
print(revenue_per_user)

print("\nOrders per user:")
print(orders_per_user)

print("\nAverage order value:")
print(avg_order_value)