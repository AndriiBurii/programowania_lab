import pandas as pd

df = pd.read_csv('demografia.csv', decimal = ',', na_values = ['NA','n/a', 'NaN',''])
print(df)
print(df.info())
print(df.head())
print(df.describe())
