import pandas as pd

df = pd.read_csv('Employee_csv')
print("\n Orignal Csv Data Frame")
print(df)

Salary = df["Salary"]
print("\n Descriptive Statistics ")

print("\n Count :-",Salary.count())
print("\n Maximum :-",Salary.max())
print("\n Minimum :-",Salary.min())
print("\n Mean :-",Salary.mean())
print("\n Mode :-",Salary.mode())
print("\n Median :-",Salary.median())
print("\n Variance :-",Salary.var())
print("\n Standard Deviation :-",Salary.std())

print("\n The Quartiles Of Salary ")
print("Q1 :- ",Salary.quantile(0.25))
print("Q2 :- ",Salary.quantile(0.50))
print("Q3 :- ",Salary.quantile(0.75))

print("\n Describe The Salary")
print(Salary.describe())