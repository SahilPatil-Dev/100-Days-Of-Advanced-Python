import pandas as pd

df = pd.read_csv("sales_data.csv")

# Total revenue column
df["revenue"] = df["quantity"] * df["price"]

# Total revenue
total_revenue = df["revenue"].sum()

# Revenue per product
revenue_per_product = df.groupby("product")["revenue"].sum()

# Highest selling product
highest_product = revenue_per_product.idxmax()

print("Total Revenue:", total_revenue)
print("\nRevenue per Product:\n", revenue_per_product)
print("\nHighest Selling Product:", highest_product)