import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(
    "../Datasets/Toyota.csv",
    index_col=0,
    na_values=["??", "???"]
)

# Remove missing values
df.dropna(inplace=True)

# Calculate average price for each age
age_price = df.groupby('Age')['Price'].mean().sort_index()

# Create Bar Plot
age_price.plot(kind='bar')

# Add title and labels
plt.title('Age Price vs Age')
plt.xlabel('Age')
plt.ylabel('Price')

# Display the graph
plt.show()
