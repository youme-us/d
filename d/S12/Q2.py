import pandas as pd
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('StudentData.csv')

print("Original Data:")
print(df)

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Fees'] = df['Fees'].fillna(df['Fees'].mean())

df = pd.get_dummies(df, columns=['City'], dtype=int)

le = LabelEncoder()
df['Admitted'] = le.fit_transform(df['Admitted'])

print("After Handling Missing Values and Encoding:")
print(df)