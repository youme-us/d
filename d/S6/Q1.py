import pandas as pd

data = {
    "Student" : ["Atharv","Darshan","Ankit","Harshal","Sarthak","Kapil","Hitesh","Krish"],
    "Course" : ["BCA","BTech","BCS","BsC","MTech","BCom","BVoC","MCA"],
    "Age" : [19,23,20,21,24,19,18,22],
    "Marks" : [95,89,91,85,76,79,84,67]
}

df = pd.DataFrame(data)

print("\nOriginal DataFrame")
print(df)

print("\nTop Five Records Of DataFrame")
print(df.head())
