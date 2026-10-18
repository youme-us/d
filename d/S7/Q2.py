import pandas as pd

Data = {
    "Name" : ["Atharv","Roshan","Darshan","Ankit","harshal"],
    "Roll No" : [47,57,74,53,85],
    "Percentage" : [95,97,78,86,85]
}

df = pd.DataFrame(Data)
print("\n --: Orignal Data Frame :--")
print(df)

Mean = df["Percentage"].mean()
Mode = df["Percentage"].mode()
Median = df["Percentage"].median()

print("\n Mean Of Data Frame",Mean)
print("\n Mode Of Data Frame",Mode)
print("\n Median Of Data Frame",Median)

