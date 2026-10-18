import numpy as np

data = np.array([3, 4, 5, 6, 7])

norm = np.sqrt(np.sum(data ** 2))
normalized = data / norm

print("Original Data:", data)
print("Length:", norm)
print("Normalized Data:", normalized)