import pandas as pd
import numpy as np
from sklearn import tree
get = tree.DecisionTreeClassifier()

dataset = pd.read_csv('Dataset3.csv')

X = dataset.iloc[:, :].values
print(X[0])
print(X[1])
print(X[7])
