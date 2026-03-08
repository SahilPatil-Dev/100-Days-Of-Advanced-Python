import matplotlib.pyplot as plt

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
sales = [12000, 4500, 6000, 7000]

plt.figure()

plt.bar(products, sales)

plt.title("Product Sales Comparison")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.show()