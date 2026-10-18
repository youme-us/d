import pandas as pd

data = {
    'rollno': [1, 2, 3, 4, 5],
    'name': ['Amit', 'Riya', 'Rahul', 'Sneha', 'Priya'],
    'mark1': [80, 75, 90, 85, 70],
    'mark2': [85, 80, 95, 75, 65],
    'mark3': [90, 70, 85, 80, 75]
}

df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)

print("Maximum Values:")
print(df.max(numeric_only=True))

print("Minimum Values:")
print(df.min(numeric_only=True))

print("Statistical Description:")
print(df.describe())

print("Shape:", df.shape)