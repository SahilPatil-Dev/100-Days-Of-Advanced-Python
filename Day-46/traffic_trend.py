import pandas as pd
import matplotlib.pyplot as plt


def plot_traffic_trend():

    data = {
        "timestamp": [
            "2024-01-01 10:00",
            "2024-01-01 11:00",
            "2024-01-01 12:00",
            "2024-01-01 13:00",
            "2024-01-01 14:00"
        ],
        "requests": [120, 200, 350, 280, 500]
    }

    df = pd.DataFrame(data)

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    plt.figure(figsize=(8,5))

    plt.plot(df["timestamp"], df["requests"], marker="o")

    plt.title("API Traffic Trend")
    plt.xlabel("Time")
    plt.ylabel("Requests")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_traffic_trend()