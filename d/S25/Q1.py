import pandas as pd

data = {
    "Product": ["Pen", "Book", "Bag", "Pencil", "Scale"],
    "Quantity": [10, 5, 2, 15, 8],
    "Price": [10, 50, 500, 5, 20]
}

df = pd.DataFrame(data)

print("Product DataFrame:")
print(df)

print("Total Quantity:", df["Quantity"].sum())
print("Average Price:", df["Price"].mean())