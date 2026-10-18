import pandas as pd

df = pd.read_csv('StudentData.csv')

print("Original Dataset:")
print(df)

df['Age'] = df['Age'].fillna(df['Age'].mean())

df['Address'] = df['Address'].fillna(df['Address'].mode()[0])

df = pd.get_dummies(df, columns=['Address'], dtype=int)

print("\nDataset after updating:")
print(df)