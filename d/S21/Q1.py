import numpy as np

marks = np.array([25, 45, 55, 65, 72, 80, 35, 90, 50, 68])

low = 0
medium = 0
high = 0

for m in marks:
    if m < 40:
        low += 1
    elif m < 70:
        medium += 1
    else:
        high += 1

print("Marks:", marks)
print("Below 40:", low)
print("40 to 69:", medium)
print("70 and above:", high)