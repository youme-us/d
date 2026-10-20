import numpy as np
import matplotlib.pyplot as plt

ages = np.array(
    
    [22, 25, 28, 30, 32,
    35, 38, 40, 42, 45,
    27, 31, 36, 48, 50]

)

print("Employee Ages:")
print(ages)

bins = [20, 30, 40, 50, 60]

frequency, bin_edges = np.histogram(ages, bins=bins)

print("\nAge Group Frequency:")
for i in range(len(frequency)):
    print(f"{bin_edges[i]}-{bin_edges[i+1]}: {frequency[i]}")

plt.hist(ages, bins=bins, color='skyblue', edgecolor='black')

plt.title("Histogram of Employee Ages")
plt.xlabel("Age Groups")
plt.ylabel("Frequency")
plt.xticks(bins)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

