import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    df = df.replace("?", pd.NA)
    df = df.dropna()
    return df

def filter_no_college(df):

    no_college = [
        "HS-grad",
        "Some-college",
        "11th",
        "10th",
        "9th",
        "12th",
        "7th-8th",
        "5th-6th",
        "1st-4th",
        "Preschool"
    ]

    return df[df["education"].isin(no_college)]
