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



sns.lmplot(x='Age', y='Price', hue='FuelType', data=df,fit_reg=True, palette='Set1')
plt.title('Age vs Price')

plt.show()




#========Lmplot with markers+++++++++++++++++

sns.lmplot(
    x='Age',
    y='Price',
    hue='FuelType',
    data=df,fit_reg=False,
    markers=["o","X","*"],
    palette='tab10'
)
plt.title('Age vs Price')
plt.show()
