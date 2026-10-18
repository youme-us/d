import numpy as np
import matplotlib.pyplot as plt

data1 = np.random.normal(50, 10, 1000)
data2 = np.random.normal(70, 15, 1000)

plt.figure(figsize=(10, 5))

plt.hist(data1, bins=20, alpha=0.6,
         edgecolor='black', label='Dataset 1')

plt.hist(data2, bins=20, alpha=0.6,
         edgecolor='red', label='Dataset 2')

plt.title("Two Normal Distributions")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()