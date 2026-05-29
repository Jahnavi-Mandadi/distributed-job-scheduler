def run(df):
    print("Transforming Data...")

    df.columns=[
        col.lower()
        for col in df.columns
    ]

    print("Column normalization complete.")

    return df