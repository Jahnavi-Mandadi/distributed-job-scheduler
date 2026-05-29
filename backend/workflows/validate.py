def run(df):
    print("Validating Data...")
    null_count=(
        df.isnull().sum().sum()
    )

    if null_count>0:
        raise Exception(
            "Null values found"
        )
    print("Validation passed")

    return df