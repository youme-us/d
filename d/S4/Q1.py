
import pandas as pd

data = {
    'Product': ['Laptop', 'Mobile', 'Keyboard', 'Mouse',
                'Monitor', 'Printer', 'Tablet', 'Speaker'],
    'Brand': ['HP', 'Samsung', 'Logitech', 'Dell',
              'LG', 'Canon', 'Apple', 'Sony'],
    'Category': ['Electronics', 'Electronics', 'Accessories',
                 'Accessories', 'Electronics', 'Electronics',
                 'Electronics', 'Accessories'],
    'Price': [55000, 25000, 1500, 800, 12000, 9000, 40000, 3000]
}

df = pd.DataFrame(data)

print("Product DataFrame:")
print(df.head())

