import pandas as pd

df = pd.read_csv("sample_data.csv")

print("Head:")
print(df.head())

print("\nInfo:")
print(df.info())

print("\nDescribe:")
print(df.describe())