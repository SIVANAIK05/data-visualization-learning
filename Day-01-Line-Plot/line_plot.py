import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset

df = pd.read_csv(
    "../datasets/Toyota.csv",
    index_col=0,
    na_values=["??", "???"]
)

# Remove missing values
df.dropna(inplace=True)

# Calculate the average price for each age
age_price = df.groupby('Age')['Price'].mean().sort_index()

# Create the line plot
plt.figure(figsize=(10, 5))
plt.plot(
    age_price.index,
    age_price.values,
    marker='o',
    color='blue'
)

# Add title and labels
plt.title("Average Car Price vs Age")
plt.xlabel("Age (Months)")
plt.ylabel("Average Price")

# Add grid
plt.grid(True)

# Display the graph
plt.show()
