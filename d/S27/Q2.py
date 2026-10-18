import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
df.to_csv("iris.csv", index=False)

df = pd.read_csv("iris.csv")

sns.jointplot(
    data=df,
    x="sepal_length",
    y="sepal_width",
    kind="kde",
    fill=True
)

plt.show()