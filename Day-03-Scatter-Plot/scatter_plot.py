import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(
    "../Datasets/Toyota.csv",
    index_col=0,
    na_values=["??", "???"]
)

# Remove missing values
df.dropna(inplace=True)

# Create Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df['Age'], df['Price'], color='black')

# Add title and labels
plt.title('Age vs Price')
plt.xlabel('Age')
plt.ylabel('Price')

# Display the graph
plt.show()
