import pandas as pd

# Simulated sales dataset (long format)
data = {
    "product": ["Laptop", "Laptop", "Laptop",
                "Mouse", "Mouse", "Mouse",
                "Keyboard", "Keyboard", "Keyboard"],
    "month": ["Jan", "Feb", "Mar",
              "Jan", "Feb", "Mar",
              "Jan", "Feb", "Mar"],
    "sales": [5000, 7000, 6500,
              1200, 1500, 1400,
              2000, 2200, 2100]
}

df = pd.DataFrame(data)

# Create pivot table
pivot_table = df.pivot_table(
    index="product",
    columns="month",
    values="sales",
    aggfunc="sum"
)

print("Pivot Table:")
print(pivot_table)