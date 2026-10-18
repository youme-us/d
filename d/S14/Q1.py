import pandas as pd

data = {
    'Name': ['Rahul', 'Amit', 'Priya', 'Sneha'],
    'Marks': [85, 90, 78, 92],
    'City': ['Nashik', 'Pune', 'Mumbai', 'Nashik']
}

df = pd.DataFrame(data)

print(df)