def clean_data(df):

    df = df[df["response_time"] >= 0]

    df["response_time"] = df["response_time"].fillna(
        df["response_time"].mean()
    )

    return df