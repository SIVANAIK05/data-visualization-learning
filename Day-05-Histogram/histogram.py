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

plt.figure(figsize=(10,10))
plt.hist(df['KM'], bins=20, color='blue', edgecolor='black' )
plt.title('Histogram of KM')
plt.xlabel('KM')
plt.ylabel('Frequency')
plt.show()
