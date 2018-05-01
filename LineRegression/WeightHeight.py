import pandas as pd
import numpy as np
from sklearn import linear_model

dataset = pd.read_csv('data.csv')

X = dataset.iloc[:, 5].values
Y = dataset.iloc[:, 6].values


X_train = X[:500].reshape((500,1)) #перевернули
X_test = X[500:].reshape((104,1))
Y_train = Y[:500]
Y_test = Y[500:]
print(len(X_train),len(X_test),len(Y_train),len(Y_test))

reg = linear_model.LinearRegression()

reg.fit(X_train,Y_train)
result = reg.predict(X_test)
print(result)
