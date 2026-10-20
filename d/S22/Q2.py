import pandas as pd

df = pd.read_csv("employee.csv")

print("DataFrame:")
print(df)

print("\nDescription:")
print(df.describe())

print("\nFirst 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

print("\nMaximum Values:")
print(df.max(numeric_only=True))

print("\nMinimum Values:")
print(df.min(numeric_only=True))