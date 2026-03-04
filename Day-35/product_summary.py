import pandas as pd

# Simulated sales dataset
data = {
    "product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse"],
    "quantity": [5, 20, 15, 3, 10],
    "price": [50000, 500, 1500, 50000, 500]
}

df = pd.DataFrame(data)

# Create revenue column
df["revenue"] = df["quantity"] * df["price"]

# Group by product
summary = (
    df.groupby("product")
      .agg(
          total_revenue=("revenue", "sum"),
          total_quantity=("quantity", "sum")
      )
      .reset_index()
      .sort_values(by="total_revenue", ascending=False)
)

print(summary)