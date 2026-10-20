import pandas as pd
import numpy as np

data = {
    "X": [2, 5, 8, 4],
    "Y": [3, 7, 6, 9]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

p1 = df.iloc[0].values
p2 = df.iloc[1].values

diff = p1 - p2

euclidean = np.sqrt(np.sum(diff ** 2))
manhattan = np.sum(np.abs(diff))

print("\nPoint 1:", p1)
print("Point 2:", p2)
print("Difference Vector:", diff)
print("Euclidean Distance:", euclidean)
print("Manhattan Distance:", manhattan)