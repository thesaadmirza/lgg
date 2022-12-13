import pandas as pd
from sklearn.model_selection import train_test_split
from src.functions import lgg, lgcg, conjunction, internal_disjunction

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('spambase_data.csv', header=None)

# Discretize the continuous features using equal-width binning
df = df.apply(pd.cut, bins=10, labels=range(10))

# Define the label column
label_column = df.columns[-1]

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=label_column), df[label_column], test_size=0.1)


def train_predict_accuracy_finder(algo=1):
    # Train the model by applying the specified algorithm to the training instances
    concept_main = list(X_train.iloc[0].dropna().items())
    for index, row in X_train.iloc[1:].iterrows():

        if algo == 2:
            concept_main = conjunction(concept_main, list(row.dropna().items()))
        elif algo == 3:
            concept_main = lgcg(concept_main, list(row.dropna().items()))
        else:
            concept_main = lgg(concept_main, list(row.dropna().items()))

    # Make predictions on the test set by comparing the test instances with the trained concept
    y_pred = []
    for index, row in X_test.iterrows():
        concept = list(row.dropna().items())
        if concept == concept_main:
            y_pred.append(y_train.iloc[0])
        else:
            y_pred.append(y_train.iloc[1])

    # Calculate the accuracy of the model
    accuracy = (y_pred == y_test).mean()
    return accuracy


accuracy = train_predict_accuracy_finder(1)
print("Accuracy LGG:", accuracy)
accuracy = train_predict_accuracy_finder(2)
print("Accuracy Conjunction:", accuracy)
accuracy = train_predict_accuracy_finder(3)
print("Accuracy Conjunction ( Internal Disjunction ):", accuracy)
