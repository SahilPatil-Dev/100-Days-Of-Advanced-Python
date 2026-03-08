import matplotlib.pyplot as plt

endpoints = ["/login", "/orders", "/profile", "/checkout"]
latency = [120, 350, 100, 420]

plt.figure()

bars = plt.bar(endpoints, latency)

plt.title("API Endpoint Latency")
plt.xlabel("Endpoint")
plt.ylabel("Average Response Time (ms)")

# Highlight slowest endpoint
max_latency = max(latency)
slowest_index = latency.index(max_latency)

bars[slowest_index].set_color("red")

plt.show()