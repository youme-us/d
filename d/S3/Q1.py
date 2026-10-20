import pandas as pd

data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Amit'],
    'Attendance': [85, 90, 78, None, 85],
    'Score': [80, None, 75, 90, 80]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

mean_score = df['Score'].mean()
df['Score'] = df['Score'].fillna(mean_score)

print("\nDataFrame after filling missing scores:")
print(df)

print("\nDuplicate Records:")
print(df.duplicated())

print("\nDuplicate Rows:")
print(df[df.duplicated()])
