import pandas as pd

data = {
    "Emp_name" : ["Atharv","Darshan","Ankit","Harshal","Sarthak","Kapil","Hitesh","Krish"],
    "Department" : ["IT","HR","Finance","Computer","IT","Finance","HR","Computer"],
    "Designation" : ["Devloper","Sales Excutive","Excutive","Recurtier","Analysist","Devloper","CA", None],
    "Salary" : [76000,49000,67000,57000,89000,78000,85000,90000]
}

df = pd.DataFrame(data)

print("\nOriginal DataFrame")
print(df)

print("\nTop Five Records Of DataFrame")
print(df.head())
