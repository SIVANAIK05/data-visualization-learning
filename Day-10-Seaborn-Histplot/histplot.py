import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(
    "../datasets/Toyota.csv",
    index_col=0,
    na_values=["??", "???"]
)

# Remove missing values
df.dropna(inplace=True)

# Histogram without KDE
sns.histplot(
    x='Price',
    hue='Automatic',
    data=df
)

plt.title('Price Distribution by Automatic Transmission')
plt.show()


# Histogram with KDE
sns.histplot(
    x='Price',
    kde=True,
    hue='Automatic',
    data=df
)

plt.title('Price Distribution by Automatic Transmission with KDE')
plt.show()
