import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')

features = ['SepalLengthCm', 'SepalWidthCm',
            'PetalLengthCm', 'PetalWidthCm']

for feature in features:
    df.boxplot(column=feature, by='Species')
    plt.title(feature + ' by Species')
    plt.suptitle('')
    plt.xlabel('Species')
    plt.ylabel(feature)
    plt.show()