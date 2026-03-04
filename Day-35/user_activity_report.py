import pandas as pd

# Simulated user logs
data = {
    "user_id": [1, 1, 2, 2, 2, 3, 3],
    "action": ["login", "view", "login", "view", "logout", "login", "view"],
    "timestamp": pd.date_range("2024-01-01", periods=7, freq="h")
}

df = pd.DataFrame(data)

# Total actions per user
actions_per_user = df.groupby("user_id")["action"].count()

print("Total actions per user:")
print(actions_per_user)

# Most frequent action per user
most_frequent_action = (
    df.groupby(["user_id", "action"])
      .size()
      .reset_index(name="count")
      .sort_values(["user_id", "count"], ascending=[True, False])
      .drop_duplicates("user_id")
)

print("\nMost frequent action per user:")
print(most_frequent_action[["user_id", "action"]])