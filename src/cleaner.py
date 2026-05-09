import pandas as pd

def clean_data(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df["Month"] = df["Date"].dt.strftime("%Y-%m")
    return df