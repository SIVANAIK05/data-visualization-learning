import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from packaging.markers import Marker

# Load dataset
 

# Load the dataset
df = pd.read_csv(
    "../Datasets/Toyota.csv",
    index_col=0,
    na_values=["??", "???"]
)

# Remove missing values
df.dropna(inplace=True)


 
#With the reg_fit 


sns.regplot(x=df['Age'], y=df['Price'])
plt.title('Age vs Price')
plt.show()


#With out reg_fit

sns.regplot(x=df['Age'], y=df['Price'], data=df, fit_reg=False)
plt.title('Age vs Price without reg')
plt.show()


 
