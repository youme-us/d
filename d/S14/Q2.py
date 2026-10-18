import pandas as pd

Data = {
    "Emp_name" : ["Atharv","Ankit","Roshan","Darshan","Hitesh"],
    "Salary" : [35000,34000,10000,23000,24000]
}

df = pd.DataFrame(Data)
df.to_csv('employee_csv', index = False)
df = pd.read_csv('employee_csv')
print("\n Orignal Csv Data Frame")
print(df)

print("Employee Data:")
print(df.head())

print("\nMean:", df['Salary'].mean())
print("Median:", df['Salary'].median())
print("Variance:", df['Salary'].var())
print("Standard Deviation:", df['Salary'].std())
print("Minimum:", df['Salary'].min())
print("Maximum:", df['Salary'].max())
print("Quartiles:")
print(df['Salary'].quantile([0.25, 0.50, 0.75]))
print("Count:", df['Salary'].count())

print("\nComplete Descriptive Statistics:")
print(df['Salary'].describe())