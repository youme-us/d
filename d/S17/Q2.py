import pandas as pd

data = {
    'Employee_ID': list(range(1, 16)),
    'Department': [
        'IT', 'HR', 'Sales', 'IT', 'HR',
        'Sales', 'IT', 'HR', 'Sales', 'IT',
        'HR', 'Sales', 'IT', 'HR', 'Sales'
    ],
    'Age': [25, 30, 28, 35, 27, 32, 29, 31, 26, 40, 33, 28, 36, 24, 38],
    'Salary': [
        30000, 25000, 28000, 40000, 27000,
        32000, 35000, 29000, 31000, 45000,
        33000, 30000, 42000, 26000, 38000
    ]
}

df = pd.DataFrame(data)

print("Employee DataFrame:")
print(df)

print("Simple Random Sampling:")
print(df.sample(n=5, random_state=1))

print("Systematic Sampling:")
print(df.iloc[::3])

print("Stratified Sampling:")
print(df.groupby('Department', group_keys=False).sample(n=1, random_state=1))