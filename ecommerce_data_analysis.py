import pandas as pd

# Load the data
data = pd.read_csv('data.csv')

# Data overview
print(data.head())        # First 5 rows
print(data.info())        # Column details
print(data.describe())    # Statistical summary
