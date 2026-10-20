import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('data.csv')

print("Original Dataset:")
print(df)

df = pd.get_dummies(df, columns=['Country'], dtype=int)

le = LabelEncoder()
df['Purchased'] = le.fit_transform(df['Purchased'])

print("Encoded Dataset:")
print(df)