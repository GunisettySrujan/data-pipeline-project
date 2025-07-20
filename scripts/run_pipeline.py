from helper_functions import validate_dataframe, save_csv, multiply_column

def extract():
    data = {'id': [1,2,3], 'value': [10,20,30]}
    df = pd.DataFrame(data)
    validate_dataframe(df)
    return df

def transform(df):
    df = multiply_column(df, 'value', 2)
    return df

def load(df):
    save_csv(df, 'output/data.csv')