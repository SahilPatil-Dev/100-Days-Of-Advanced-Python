import matplotlib.pyplot as plt

# Simulated monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [5000, 7000, 6500, 8000, 7500, 9000]

plt.figure()

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Revenue")

plt.grid(True)

plt.show()