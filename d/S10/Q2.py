import pandas as pd

df = pd.read_csv('Student_Marks.csv')

print("Before Discretization:")
print(df)

bins = [-1, 40, 60, 80, 100]
labels = ['Poor', 'Average', 'Good', 'Excellent']

df['Performance'] = pd.cut(df['Marks'], bins=bins, labels=labels)

print("\nAfter Discretization:")
print(df)