import pandas as pd
from sklearn.model_selection import train_test_split


# Load the dataset into a Pandas DataFrame
df = pd.read_csv('spambase_data.csv', header=None)

# Discretize the continuous features using equal-width binning
df = df.apply(pd.cut, bins=10, labels=range(10))

# Define the label column
label_column = df.columns[-1]

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=label_column), df[label_column], test_size=0.1)

