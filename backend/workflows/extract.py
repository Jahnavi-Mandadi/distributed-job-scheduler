import pandas as pd

def run():
    print("Extracting CSV....")

    df=pd.read_csv("data/hotel_bookings.csv")

    print(f"Rows Extracted:{len(df)}")

    return df 