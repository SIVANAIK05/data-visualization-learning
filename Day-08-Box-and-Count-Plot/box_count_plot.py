
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
#==========================COUNT PLOT==================

#sns.countplot(x='FuelType',  data=df)
sns.countplot(x='FuelType', hue='Automatic' ,data=df)
plt.title('Age vs Price')
plt.show()


#======================BOX PLOT======================

sns.boxplot(x='Price',  hue='Automatic',data=df)
plt.title('Age vs Price')
plt.show()

