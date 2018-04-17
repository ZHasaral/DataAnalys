import pandas as pd
import numpy as np
from sklearn import tree
get = tree.DecisionTreeClassifier()

dataset = pd.read_csv('Churn_Modelling.csv')

X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values
print(X[0])
print(X[1])
print(X[7])


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])



onehotencoder = OneHotEncoder(categorical_features = [1,2])
X = onehotencoder.fit_transform(X).toarray()


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

print(X[0])
print(X[1])
print(X[7])

get = get.fit(X,y)

#result = get.predict([[input(),input(),input(),input(),input(),input(),input(),input(),input(),input()]])
# result = get.predict([[619,0,0,42,2,0.0,1,1,1,101348.88]])
result = get.predict([[608,2,0,41,1,83807.86,1,0,1,112542.58]])
print(result)

