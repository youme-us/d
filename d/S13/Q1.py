import pandas as pd

Data = {
    "Name" : ["Atharv","Roshan",None,"Ankit","harshal"],
    "Roll No" : [47,57,74,None,85],
    "Percentage" : [95,97,78,86,None]
}

df = pd.DataFrame(Data)
print("\n Orignal Data Frame ")
print(df)

print("\n Shape Of Data Frame")
print(df.shape)

print("\n Size Of Data Frame")
print(df.size)

print("\n Dtypes Of Data Frame")
print(df.dtypes)

print("\n Decscribe of Data Frame")
print(df.describe())

print("\n Length Of Data Frame")
print(len(df))

print("\n Missing Values Of Data Frame")
print(df.isnull().sum())