import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('StudentData.csv')
print("\nOrignal DataSet")
print(df)

df_Encoded = pd.get_dummies(df, columns = ["Name"], dtype = int)
print("\nAfter One_Hot Encoding")
print(df_Encoded)

le = LabelEncoder()
df_Encoded['Class'] = le.fit_transform(df_Encoded['Class'])
print("\nAfter Label Encoding")
print(df_Encoded)