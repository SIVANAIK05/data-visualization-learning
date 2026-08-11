
import pandas as pd


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    r' "../datasets/Toyota.csv"',
    index_col=0,
    na_values=["??", "???"]
)
# Remove missing values
df.dropna(inplace=True)

corr_matrix = df.select_dtypes(include=[np.number]).corr()

plt.figure(figsize=(10, 8))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")
plt.show()
