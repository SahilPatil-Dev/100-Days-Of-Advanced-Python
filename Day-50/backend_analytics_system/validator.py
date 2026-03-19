def validate_data(df):

    df = df[
        df["status_code"].between(100, 599)
    ]

    df = df[df["endpoint"].notna()]

    return df