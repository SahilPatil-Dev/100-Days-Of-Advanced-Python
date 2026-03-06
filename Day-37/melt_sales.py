import pandas as pd

# Wide format dataset
data = {
    "product": ["Laptop", "Mouse", "Keyboard"],
    "Jan": [5000, 1200, 2000],
    "Feb": [7000, 1500, 2200],
    "Mar": [6500, 1400, 2100]
}

df = pd.DataFrame(data)

# Convert wide → long format
long_df = pd.melt(
    df,
    id_vars="product",
    var_name="month",
    value_name="sales"
)

print("Long Format Data:")
print(long_df)