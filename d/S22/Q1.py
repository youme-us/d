import pandas as pd

subjects = ["Python", "DBMS", "Java", "Statistics", "Web Design"]
marks = [85, 78, 90, 75, 88]

data = {
    "Subject": subjects,
    "Marks": marks
}

df = pd.DataFrame(data)

print(df)