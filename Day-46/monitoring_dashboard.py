import pandas as pd
import matplotlib.pyplot as plt


def monitoring_dashboard():

    # Simulated traffic data
    traffic_data = {
        "hour": ["10:00","11:00","12:00","13:00","14:00"],
        "requests": [120, 200, 350, 280, 500]
    }

    # Endpoint metrics
    endpoint_data = {
        "endpoint": ["/login", "/orders", "/profile", "/checkout"],
        "avg_latency": [120, 340, 90, 410],
        "error_rate": [0.01, 0.05, 0.02, 0.08]
    }

    traffic_df = pd.DataFrame(traffic_data)
    endpoint_df = pd.DataFrame(endpoint_data)

    fig, axes = plt.subplots(3, 1, figsize=(8,12))

    # Traffic trend
    axes[0].plot(traffic_df["hour"], traffic_df["requests"], marker="o")
    axes[0].set_title("Requests Per Hour")
    axes[0].set_xlabel("Hour")
    axes[0].set_ylabel("Requests")

    # Latency comparison
    axes[1].bar(endpoint_df["endpoint"], endpoint_df["avg_latency"])
    axes[1].set_title("Average Latency per Endpoint")
    axes[1].set_ylabel("Latency (ms)")

    # Error rate
    axes[2].bar(endpoint_df["endpoint"], endpoint_df["error_rate"])
    axes[2].set_title("Error Rate per Endpoint")
    axes[2].set_ylabel("Error Rate")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    monitoring_dashboard()