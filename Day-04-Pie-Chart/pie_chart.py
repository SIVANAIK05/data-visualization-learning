
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(
    "../Datasets/Toyota.csv",
    index_col=0,
    na_values=["??", "???"]
)

df.dropna(inplace=True)

# Count the number of cars for each fuel type
fuel_counts = df['FuelType'].value_counts()

# Create Pie Chart
fuel_counts.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    figsize=(8, 8)
)

plt.title('Fuel Type Distribution')
plt.ylabel('')
plt.show()
