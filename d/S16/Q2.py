import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    'Country': ['India', 'USA', 'France', 'India', 'USA', 'France'],
    'Purchased': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

df = pd.read_csv('data.csv')

print("Original Dataset:")
print(df)

df = pd.get_dummies(df, columns=['Country'], dtype=int)

le = LabelEncoder()
df['Purchased'] = le.fit_transform(df['Purchased'])

print("Encoded Dataset:")
print(df)