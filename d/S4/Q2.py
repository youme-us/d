
import pandas as pd

df = pd.read_csv('StudentData.csv')

print("\nOriginal Dataset:")
print(df)

mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

print("\nDataset after replacing missing Age:")
print(df)

df.to_csv('StudentData.csv', index=False)

print("\nUpdated dataset saved successfully!")
