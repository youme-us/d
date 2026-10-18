import pandas as pd

Data = {
    "Name" : ["Atharv","Roshan","Darshan","Ankit","harshal"],
    "Roll No" : [47,57,74,53,85],
    "Marks" : [95,97,78,86,85]
}

df = pd.DataFrame(Data)
print("\n Orignal Data Frame")
print(df)

print("\n Mean :- ",df["Marks"].mean())
print("\n Median :- ",df["Marks"].median())
print("\n Mode :- ",df["Marks"].mode())
