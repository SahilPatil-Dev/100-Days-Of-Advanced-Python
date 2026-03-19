import json

def export_reports(df):

    df.to_csv("report.csv", index=False)

    records = df.to_dict(orient="records")

    with open("report.json", "w") as f:
        json.dump(records, f, indent=2, default=str)