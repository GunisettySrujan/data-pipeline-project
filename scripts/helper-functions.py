# helper_functions.py

def validate_dataframe(df):
    """Check if DataFrame is empty and has required columns."""
    if df.empty:
        raise ValueError("DataFrame is empty!")
    required_columns = ['id', 'value']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
    return True

def save_csv(df, path):
    """Save DataFrame to CSV and print confirmation."""
    df.to_csv(path, index=False)
    print(f"Saved DataFrame to {path}")

def multiply_column(df, column, factor):
    """Multiply a numeric column by a factor."""
    if column in df.columns:
        df[column] = df[column] * factor
    else:
        print(f"Column {column} not found in DataFrame.")
    return df