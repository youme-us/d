import pandas as pd

df = pd.read_csv('StudentData.csv')

print("Student Dataset:")
print(df)

print("\nStatistical Description:")
print(df.describe())

print("\nShape of Dataset:")
print(df.shape)

print("\nFirst Two Rows:")
print(df.head(2))