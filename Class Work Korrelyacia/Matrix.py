#Корреляционная матрица
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
df = pd.DataFrame({'a': np.random.randint(0, 50, 1000)})
df['b'] = df['a'] + np.random.normal(0, 10, 1000) # positively correlated with 'a'
df['c'] = 100 - df['a'] + np.random.normal(0, 5, 1000) # negatively correlated with 'a'
df['d'] = np.random.randint(0, 50, 1000) # not correlated with 'a'
print(df.corr())
pd.scatter_matrix(df, figsize=(6, 6))
plt.show()
