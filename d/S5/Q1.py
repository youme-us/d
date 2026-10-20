import pandas as pd

data = {
    'Laptop_Model': ['HP', 'Dell', 'Lenovo', 'Asus', 'Acer'],
    'Cost': [50000, 60000, 45000, 55000, 40000]
}

df = pd.DataFrame(data)

print(df)