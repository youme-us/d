import pandas as pd

Marks = [72,85,91,68,85,79,94]

s = pd.Series(Marks)
print("\nOrignal Series :-")
print(s)

print("\nSum Of Series :-",s.sum())
print("\nAverage Of Series ;-",s.mean())
print("\nMedian Of Series :-",s.median())
print("\nMode Of Series :-",s.mode())
print("\nMaximum Of Series ;-",s.max())
print("\nMinimum Of Series :-",s.min())
print("\nStandard Deviation :-",s.std())