import numpy as np


# Simulated monthly sales (12 months)
sales = np.array([12000, 15000, 18000, 13000, 17000, 20000,
                  21000, 19000, 22000, 24000, 23000, 25000])

# Total sales
total_sales = np.sum(sales)

# Monthly average
monthly_average = np.mean(sales)

# Highest month
highest_month_index = np.argmax(sales)
highest_month_value = sales[highest_month_index]

print("Total sales:", total_sales)
print("Monthly average:", monthly_average)
print("Highest month index:", highest_month_index)
print("Highest month sales:", highest_month_value)