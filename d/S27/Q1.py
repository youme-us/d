import pandas as pd

data = {
    "Category": ["A", "B", "C", "D", "E"],
    "Value": [25, 60, 15, 80, 40]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("Maximum Value:", df["Value"].max())
print("Minimum Value:", df["Value"].min())