import pandas as pd
import numpy as np

sales = [20, 25, 30, 28, 35, 40, 38, 45, 50, 42, 48, 55]

df = pd.DataFrame({'Monthly_Sales': sales})

print(df)
print("Range:", df['Monthly_Sales'].max() - df['Monthly_Sales'].min())
print("Variance:", np.var(sales))
print("Standard Deviation:", np.std(sales))