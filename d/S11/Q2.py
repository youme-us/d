import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Species': ['setosa'] * 50 + ['versicolor'] * 50 + ['virginica'] * 50,
    'SepalLength': [5.1] * 50 + [6.0] * 50 + [6.5] * 50
}

df = pd.DataFrame(data)
df.to_csv('iris.csv', index=False)

df = pd.read_csv('iris.csv')

frequency = df['Species'].value_counts()

plt.bar(frequency.index, frequency.values)
plt.title("Frequency of Iris Species")
plt.xlabel("Species")
plt.ylabel("Frequency")
plt.show()

for species in df['Species'].unique():
    plt.hist(df[df['Species'] == species]['SepalLength'], alpha=0.5, label=species)

plt.title("Histogram of Iris Species")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.legend()
plt.show()