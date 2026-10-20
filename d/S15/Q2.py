import pandas as pd

df = pd.read_csv('data.csv')

print("DataFrame:")
print(df)

print("Description:")
print(df.describe())

print("First 5 Rows:")
print(df.head())

print("Last 5 Rows:")
print(df.tail())

print("Maximum Values:")
print(df.max(numeric_only=True))

print("Minimum Values:")
print(df.min(numeric_only=True))