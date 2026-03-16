import pandas as pd
import matplotlib.pyplot as plt


def plot_endpoint_latency():

    data = {
        "endpoint": ["/login", "/orders", "/profile", "/checkout"],
        "avg_latency": [120, 340, 90, 410]
    }

    df = pd.DataFrame(data)

    plt.figure(figsize=(8,5))

    plt.bar(df["endpoint"], df["avg_latency"])

    plt.title("Average Endpoint Latency")
    plt.xlabel("Endpoint")
    plt.ylabel("Latency (ms)")

    plt.show()


if __name__ == "__main__":
    plot_endpoint_latency()